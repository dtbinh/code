import numpy as _np
import mathphys as _mp

#Simulations of the phase deviation caused by the transient beam loading  in a 3rd harmonic cavity system
# param - list of ring parameters
    f_res=f_rf-param['Detune0'] #Generator Frequency
    h=int(param['hh'])        # harmonic number of the main RF
    U0=param['Cgamma']/(2*pi)*(param['En']/1e+9)**4*param['I2']*1e+06
    Js=2+param['I4']/param['I2']
    taus=(2*E*param['C'])/(Js*U0*param['cluz'])
    lambdas = 2/taus


    # Theoretical 3rd harmonic cavity voltage
    Vgh=Vrf*sqrt(1/m**2-(U0/Vrf)**2/(m**2-1)) #(kV)

    w_res=2*pi*f_res

    #Vectors definition
    phi=_np.zeros((n_voltas_max+1,h))
    Vtot=_np.zeros(h)
    Vharm=_np.zeros(h)
    Vmain=_np.zeros(h)
    phimain=_np.zeros(h)
    phih=_np.zeros(h)
    phi_final=_np.zeros(h)
    delta_final=_np.zeros(h)
    Vbn=_np.zeros((h),dtype=complex)
    VmainC=_np.zeros((h),dtype=complex)


    tot=0
    for i in range(len(gap)):
        I0[ini:(gap[i][0])]=gap[i][1]
        ini=gap[i][0]

    n_bunches=int(_np.sum(I0))
    print ("Total number of filled bunches : {0:3d}" .format(n_bunches))


    #Loss Current
    #Loaded Angle
    PhiL=atan2((tan(Psi)-2*I_tot/I_0*cos(Phi_sync)),(1+2*I_tot/I_0*sin(Phi_sync)))
    #LossFactor
    #Detune

    print ('-----------------------------------------------')
    print ('Main parameters for calculation')
    print ('Optimum Detune = {0:0.3f} kHz' .format(2*I_tot/(Vrf*1000)*param['Rs0']/(1+param['betac'])*cos(pi-Phi_sync)*f_rf/(2*QL)*1e-3))
    print ('Generator voltages (1) Acc. and (2) HHC:')
    print ('Total number of filled bunches = {0:3.0f}' .format(n_bunches))

    #Tracking
            for p in range(h):
                phi[0][p]=phi[n_voltas_max][p]
        print ('        phi(first bucket) = {1:0.3e} and phi(last bucket) = {1:0.3e}'.format(phi[0][1],phi[0][n_bunches-1]))
        for n in range(1,n_voltas_max+1): #loop in turns
            for p in range(h):# loop in bunches
                phi[n][p]=phi[n-1][p]+2*pi* alfa*h*delta[n-1][p]
                if (p==0 and n==1 and l==0): # first turn of the first particle
                    Vb[p]=-(k0*I0[p]/f0)/1000
                elif (p==0):# other turns for first particles
                    Dt=(phi[n][0]-phi[n-1][h-1])/w_rf+2*pi/w_rf
                    Vb[0]=(Vb[h-1]-(k0*I0[h-1]/f0)/1000)*complex(cos(w_res*Dt),sin(w_res*Dt))*exp(-w_res*Dt/(2*QL))-(k0*I0[0]/f0)/1000
                    Vbn[0]=(Vbn[h-1]-(kn*I0[h-1]/f0)/1000)*complex(cos(w_resn*Dt),sin(w_resn*Dt))*exp(-w_resn*Dt/(2*param['Q0n']))-(kn*I0[0]/f0)/1000
                else:# other turns for all other particles
                    Dt=(phi[n][p]-phi[n][p-1])/w_rf+2*pi/w_rf
                    Vb[p]=(Vb[p-1]-(k0*I0[p-1]/f0)/1000)*complex(cos(w_res*Dt),sin(w_res*Dt))*exp(-w_res*Dt/(2*QL))-(k0*I0[p]/f0)/1000
                    Vbn[p]=(Vbn[p-1]-(kn*I0[p-1]/f0)/1000)*complex(cos(w_resn*Dt),sin(w_resn*Dt))*exp(-w_resn*Dt/(2*param['Q0n']))-(kn*I0[p]/f0)/1000

                Vtot[p]=Vg0*_np.sin(pi-Phi_sync+phi[n][p]+Psi-PhiL)+_np.real(Vb[p]+Vbn[p])
            if (n==n_voltas_max):
                phi_final=phi[n]
                delta_final=delta[n]
    #Harmonic voltage and phase
    Vharm=_np.absolute(Vbn)
    phih=pi/2+_np.angle(Vbn)
    #Main voltage and final synchronous phase
    VmainC=Vg0*complex(sin(pi-Phi_sync+phi_final[p]+Psi-PhiL),cos(pi-Phi_sync+phi_final[p]+Psi-PhiL))+Vb
    phimain=pi/2-_np.angle(VmainC)

    f=open('Landau.txt','w')
    f.write('I0[mA] \t Vharm[kV] \t phi_harm [rad] \t Vmain[kV] \t phi_main [rad] \t phi_final [rad] \t delta_final\n')
    for j in range(h):
        f.write(str('{0:0.5e}'.format(I0[j])) + '\t')
        f.write(str('{0:0.5e}'.format(Vharm[j])) + '\t')
        f.write(str('{0:0.5e}'.format(phih[j])) + '\t')
        f.write(str('{0:0.5e}'.format(Vmain[j])) + '\t')
        f.write(str('{0:0.5e}'.format(phimain[j])) + '\t')
        f.write(str('{0:0.5e}'.format(phi_final[j])) + '\t')
        f.write(str('{0:0.5e}'.format(delta_final[j])) + '\t')
        f.write(str('{0:0.5e}'.format(abs(Vb[j]))) + '\t')
        f.write(str('{0:0.5e}'.format(phase(Vb[j]))) + '\t')
        f.write('\n')
    f.close()
    print('Data saved in file: Landau.txt \n')