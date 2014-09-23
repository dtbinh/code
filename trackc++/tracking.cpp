#include "trackc++.h"
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_permutation.h>
#include <gsl/gsl_linalg.h>

// track_findm66
// -------------
// returns a vector with 6-d transfer matrices, one for each element
//
// inputs:
//		line:	 		Element vector representing the beam transport line
//		closed_orbit:	Pos vector representing calculated closed orbit.
//
// outputs:
//		m66:			vector of (double*)-type elements. Each elements if a pointer
//						to a flat c array with 36 elements representing the transfer element of
//						that element. The matrix is is row-format: (drx_f/drx_i, drx_f/dpx_i, ..., dl_f/de_i, dl_f/dl_i)
//						===========
//						ATTENTION: !!! Memory for each matrix is supposed to be previously allocated !!!
//						===========
//		RETURN:			status do tracking (see 'auxiliary.h')


Status::type track_findm66 (const Accelerator& accelerator, const std::vector<Pos<double> >& closed_orbit, std::vector<double*> m66) {

	Status::type status  = Status::success;
	const std::vector<Element>& lattice = accelerator.lattice;

	// checks consistency of data
	if (m66.size() != lattice.size()) {
		status = Status::inconsistent_dimensions;
		return status;
	}

	for(unsigned int i=0; i<lattice.size(); ++i) {

		Pos<Tpsa<6,1> > tpsa;
		tpsa.rx = Tpsa<6,1>(closed_orbit[i].rx, 0); tpsa.px = Tpsa<6,1>(closed_orbit[i].px, 1);
		tpsa.ry = Tpsa<6,1>(closed_orbit[i].ry, 2); tpsa.py = Tpsa<6,1>(closed_orbit[i].py, 3);
		tpsa.de = Tpsa<6,1>(closed_orbit[i].de, 4); tpsa.dl = Tpsa<6,1>(closed_orbit[i].dl, 5);

		// track through element
		if ((status = track_elementpass (lattice[i], tpsa, accelerator)) != Status::success) return status;

		// minimum  check to see if memory of allocated for each transfer matrix
		if (m66[i] == NULL) {
			status = Status::uninitialized_memory;
			return status;
		}

		// RX
		*(m66[i] + 0*6+0) = tpsa.rx.c[1];*(m66[i] + 0*6+1) = tpsa.rx.c[2];
		*(m66[i] + 0*6+2) = tpsa.rx.c[3];*(m66[i] + 0*6+3) = tpsa.rx.c[4];
		*(m66[i] + 0*6+4) = tpsa.rx.c[5];*(m66[i] + 0*6+5) = tpsa.rx.c[6];
		// PX
		*(m66[i] + 1*6+0) = tpsa.px.c[1];*(m66[i] + 1*6+1) = tpsa.px.c[2];
		*(m66[i] + 1*6+2) = tpsa.px.c[3];*(m66[i] + 1*6+3) = tpsa.px.c[4];
		*(m66[i] + 1*6+4) = tpsa.px.c[5];*(m66[i] + 1*6+5) = tpsa.px.c[6];
		// RY
		*(m66[i] + 2*6+0) = tpsa.ry.c[1];*(m66[i] + 2*6+1) = tpsa.ry.c[2];
		*(m66[i] + 2*6+2) = tpsa.ry.c[3];*(m66[i] + 2*6+3) = tpsa.ry.c[4];
		*(m66[i] + 2*6+4) = tpsa.ry.c[5];*(m66[i] + 2*6+5) = tpsa.ry.c[6];
		// PY
		*(m66[i] + 3*6+0) = tpsa.py.c[1];*(m66[i] + 3*6+1) = tpsa.py.c[2];
		*(m66[i] + 3*6+2) = tpsa.py.c[3];*(m66[i] + 3*6+3) = tpsa.py.c[4];
		*(m66[i] + 3*6+4) = tpsa.py.c[5];*(m66[i] + 3*6+5) = tpsa.py.c[6];
		// DE
		*(m66[i] + 4*6+0) = tpsa.de.c[1];*(m66[i] + 4*6+1) = tpsa.de.c[2];
		*(m66[i] + 4*6+2) = tpsa.de.c[3];*(m66[i] + 4*6+3) = tpsa.de.c[4];
		*(m66[i] + 4*6+4) = tpsa.de.c[5];*(m66[i] + 4*6+5) = tpsa.de.c[6];
		// DL
		*(m66[i] + 5*6+0) = tpsa.dl.c[1];*(m66[i] + 5*6+1) = tpsa.dl.c[2];
		*(m66[i] + 5*6+2) = tpsa.dl.c[3];*(m66[i] + 5*6+3) = tpsa.dl.c[4];
		*(m66[i] + 5*6+4) = tpsa.dl.c[5];*(m66[i] + 5*6+5) = tpsa.dl.c[6];

	}

	return status;

}

Status::type track_findorbit6(
		const Accelerator& accelerator,
		std::vector<Pos<double> >& cod) {

	const std::vector<Element>& the_ring = accelerator.lattice;

	double delta        = 1e-9;              // [m],[rad],[dE/E]
	double tolerance    = 2.22044604925e-14;
	int    max_nr_iters = 50;

	// calcs longitudinal fixed point
	double L0 = latt_findspos(the_ring, 1+the_ring.size());
	double T0 = L0 / light_speed;
	std::vector<int>    cav_idx = latt_findcells_frequency(the_ring, 0, true);
	double frf = the_ring[cav_idx[0]].frequency;
	double fixedpoint = light_speed*((1.0*accelerator.harmonic_number)/frf - T0);

	// temporary vectors and matrices
	std::vector<Pos<double> > co(7,0);
	std::vector<Pos<double> > co2(7,0);
	std::vector<Pos<double> > D(7,0);
	std::vector<Pos<double> > M(6,0);
	Pos<double> dco(1.0,1.0,1.0,1.0,1.0,1.0);
	Pos<double> theta(0.0,0.0,0.0,0.0,0.0,0.0);

	theta.dl = fixedpoint;
	matrix6_set_identity(D, delta);

	int nr_iter = 0;
	while ((get_max(dco) > tolerance) and (nr_iter <= max_nr_iters)) {
		co = co + D;
		Pos<double> Ri = co[6];
		std::vector<Pos<double> > co2;
		unsigned int element_offset = 0;
		Plane::type lost_plane;
		Status::type status = Status::success;
		status = (Status::type) ((int) status | (int) track_linepass(accelerator, co[0], co2, element_offset, lost_plane, false));
		status = (Status::type) ((int) status | (int) track_linepass(accelerator, co[1], co2, element_offset, lost_plane, false));
		status = (Status::type) ((int) status | (int) track_linepass(accelerator, co[2], co2, element_offset, lost_plane, false));
		status = (Status::type) ((int) status | (int) track_linepass(accelerator, co[3], co2, element_offset, lost_plane, false));
		status = (Status::type) ((int) status | (int) track_linepass(accelerator, co[4], co2, element_offset, lost_plane, false));
		status = (Status::type) ((int) status | (int) track_linepass(accelerator, co[5], co2, element_offset, lost_plane, false));
		status = (Status::type) ((int) status | (int) track_linepass(accelerator, co[6], co2, element_offset, lost_plane, false));
		if (status != Status::success) {
			return Status::findorbit_one_turn_matrix_problem;
		}
		//print(co2);
		Pos<double> Rf = co2[6];
		M[0] = (co2[0] - Rf) / delta;
		M[1] = (co2[1] - Rf) / delta;
		M[2] = (co2[2] - Rf) / delta;
		M[3] = (co2[3] - Rf) / delta;
		M[4] = (co2[4] - Rf) / delta;
		M[5] = (co2[5] - Rf) / delta;
		//print(M);
		Pos<double> b = Rf - Ri - theta;
		std::vector<Pos<double> > M_1(6,0);
		matrix6_set_identity(M_1);
		M_1 = M_1 - M;
		dco = linalg_solve(M_1, b);
		co[6] = dco + Ri;
		co[0] = co[6]; co[1] = co[6];
		co[2] = co[6]; co[3] = co[6];
		co[4] = co[6]; co[5] = co[6];
		nr_iter++;
	}

	if (nr_iter > max_nr_iters) {
		return Status::findorbit_not_converged;
	}

	// propagates fixed point throught the_ring
	cod.clear();
	unsigned int element_offset = 0;
	Plane::type lost_plane;
	track_linepass(accelerator, co[6], cod, element_offset, lost_plane, true);
	cod.pop_back(); // eliminates last element which is the same as first
	return Status::success;

}


Pos<double> linalg_solve(const std::vector<Pos<double> >& M, const Pos<double>& B) {

	gsl_matrix* m = gsl_matrix_alloc(6,6);
	gsl_vector* b = gsl_vector_alloc(6);
	gsl_vector* x = gsl_vector_alloc(6);
	gsl_permutation* p = gsl_permutation_alloc(6);

	gsl_vector_set(b,0,B.rx); gsl_vector_set(b,1,B.px);
	gsl_vector_set(b,2,B.ry); gsl_vector_set(b,3,B.py);
	gsl_vector_set(b,4,B.de); gsl_vector_set(b,5,B.dl);
	for(unsigned int i=0; i<6; ++i) {
		gsl_matrix_set(m,0,i,M[i].rx); gsl_matrix_set(m,1,i,M[i].px);
		gsl_matrix_set(m,2,i,M[i].ry); gsl_matrix_set(m,3,i,M[i].py);
		gsl_matrix_set(m,4,i,M[i].de); gsl_matrix_set(m,5,i,M[i].dl);
	}

	int s; gsl_linalg_LU_decomp(m, p, &s);
	gsl_linalg_LU_solve(m, p, b, x);
	Pos<double> X(gsl_vector_get(x,0),gsl_vector_get(x,1),gsl_vector_get(x,2),gsl_vector_get(x,3),gsl_vector_get(x,4),gsl_vector_get(x,5));

	gsl_matrix_free(m);
	gsl_vector_free(b);
	gsl_vector_free(x);
	gsl_permutation_free(p);
	return X;
}
