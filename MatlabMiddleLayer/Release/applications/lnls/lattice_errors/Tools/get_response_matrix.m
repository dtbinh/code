function MR = get_response_matrix(the_ring, bpms, hcms, vcms, dim)
% M(y,x) --> y : orbit    x: corrector

if ~exist('dim','var'), dim = get_dim(the_ring); end

if strcmp(dim,'6d')
    [M, T] = findm66(the_ring, 1:length(the_ring)+1);
else
    [M, T] = findm44(the_ring,0,1:length(the_ring)+1);
end

len_hcms = size(hcms,1);
len_vcms = size(vcms,1);
len_bpms = size(bpms,1);

mxx = zeros(len_bpms, len_hcms);
myx = zeros(len_bpms, len_hcms);
mxy = zeros(len_bpms, len_vcms);
myy = zeros(len_bpms, len_vcms);

for i=1:len_bpms
    for j=1:len_hcms
        [cxx, cyx, ~, ~] = get_C(M,T,bpms(i,:),hcms(j,:),the_ring(hcms(j,:)));
        mxx(i,j) = cxx;
        myx(i,j) = cyx;
    end
    for j=1:len_vcms
        [~, ~, cxy, cyy] = get_C(M,T,bpms(i,:),vcms(j,:),the_ring(vcms(j,:)));
        mxy(i,j) = cxy;
        myy(i,j) = cyy;
    end
end

MR = [mxx, mxy; myx, myy];

% step_kick = 0.00001;
% % if no_print, lnls_create_waitbar('Calcs H-COD Response Matrix',0.5,len_hcm); end
% for i=1:len_hcms
%     idx = hcms(i);
%     init_hkick = lnls_get_kickangle(the_ring, idx, 'x');
%     the_ring = lnls_set_kickangle(the_ring, init_hkick - 0.5* step_kick, idx, 'x');
%     [codx1, cody1] = calc_cod(the_ring);
%     the_ring = lnls_set_kickangle(the_ring, init_hkick + 0.5* step_kick, idx, 'x');
%     [codx2, cody2] = calc_cod(the_ring);
%     the_ring = lnls_set_kickangle(the_ring, init_hkick, idx, 'x');
%     mxx(:,i) = (codx2(bpms) - codx1(bpms)) / step_kick;
%     myx(:,i) = (cody2(bpms) - cody1(bpms)) / step_kick;
% %     M = bpm_g(:,:,i)*[cxy;cyy]*vcm_g(j);
% %     mxy(i,j) = M(1);
% %     myy(i,j) = M(2);
% %     if no_print, lnls_update_waitbar(i); end
% end
% % if no_print, lnls_delete_waitbar; end
% % if no_print, lnls_create_waitbar('Calcs V-COD Response Matrix',0.5,len_vcm); end
% for i=1:len_vcms
%     idx = vcms(i);
%     init_vkick = lnls_get_kickangle(the_ring, idx, 'y');
%     the_ring = lnls_set_kickangle(the_ring, init_vkick - 0.5* step_kick, idx, 'y');
%     [codx1, cody1] = calc_cod(the_ring);
%     the_ring = lnls_set_kickangle(the_ring, init_vkick + 0.5* step_kick, idx, 'y');
%     [codx2, cody2] = calc_cod(the_ring);
%     the_ring = lnls_set_kickangle(the_ring, init_vkick, idx, 'y');
%     mxy(:,i) = (codx2(bpms) - codx1(bpms)) / step_kick;
%     myy(:,i) = (cody2(bpms) - cody1(bpms)) / step_kick;
% %     M = bpm_g(:,:,i)*[cxy;cyy]*vcm_g(j);
% %     mxy(i,j) = M(1);
% %     myy(i,j) = M(2);
% %     if no_print, lnls_update_waitbar(i); end
% end
% % if no_print, lnls_delete_waitbar; end
% M = [mxx, mxy; myx, myy];


function [cxx, cyx, cxy, cyy] = get_C(M,T,i,j,segmented_element)
% cxy --> orbit at bpm x due to kick in corrector y

R_j = T(:,:,j(end));
R_i = T(:,:,i(end));
M_i = R_i * M / R_i;
if (i(end)>j(end))   
    R_ij = R_i/R_j;
else
    R_ij = R_i * (T(:,:,end) / R_j);
end
%C = R_ij / (diag([1 1 1 1])-M44);
D = diag(ones(1,size(M,1)));
C = (D - M_i) \ R_ij;

total_length = sum(getcellstruct(segmented_element, 'Length', 1:length(segmented_element)));
cxx = (total_length/2) * C(1,1) + C(1,2);
cyx = (total_length/2) * C(3,1) + C(3,2);
cxy = (total_length/2) * C(1,3) + C(1,4);
cyy = (total_length/2) * C(3,3) + C(3,4);