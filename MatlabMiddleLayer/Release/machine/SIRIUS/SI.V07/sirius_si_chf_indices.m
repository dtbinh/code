function idx = sirius_si_chf_indices(the_ring)

idx = [];
idx = [idx findcells(the_ring, 'FamName', 'cf')];
idx = sort(idx);
