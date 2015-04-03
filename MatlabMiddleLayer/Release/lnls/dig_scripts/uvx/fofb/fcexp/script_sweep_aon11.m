deltarf = 1e-3; % MHz
gap_vel = 60;
phase_vel = 30;

aon11_gaps = [repmat(22,5,1); repmat(26,5,1); repmat(29,5,1); repmat(33, 5,1)];
aon11_phases = repmat([-25; -15; -10; -5; 0; 5; 10; 15; 25], 4,1);

switch2online;

aon11_gap0 = getpv('AON11GAP_SP');
aon11_phase0 = getpv('AON11FASE_SP');
aon11_gapv0 = getpv('AON11VGAP_SP');
aon11_phasev0 = getpv('AON11VFASE_SP');

setpv('AON11VGAP_SP', gap_vel);
setpv('AON11VFASE_SP', phase_vel);

nu = zeros(length(aon11_gaps), 2);

lnls1_fast_orbcorr_enable_excitation;

for i=1:length(aon11_gaps)
    if getpv('AON11GAP_SP') ~= aon11_gaps(i)
        setpv('AON11GAP_SP', aon11_gaps(i));
    end
    pause(10);
    
    if getpv('AON11FASE_SP') ~= aon11_phases(i)
        setpv('AON11FASE_SP', aon11_phases(i));
    end
    pause(10);
    
    % Turn FOFB temporarily on to correct orbit to reference
    lnls1_fast_orbcorr_on;
    pause(1);
    lnls1_fast_orbcorr_off;
    pause(2);
    
    % Perform response matrix measurement via FOFB Fast Command
    fcexprespm;
    
    % Change RF frequency to measure dispersion orbit
    pause(1);
    frf = getrf;
    setrf(frf-deltarf/2);
    pause(4);
    setrf(frf+deltarf/2);
    pause(4);
    setrf(frf);
    pause(2);
    
    nu(i,:) = gettune;
end

lnls1_fast_orbcorr_disable_excitation;

getpv('AON11GAP_SP', aon11_gap0);
getpv('AON11FASE_SP', aon11_phase0);
getpv('AON11VGAP_SP', aon11_gapv0);
getpv('AON11VFASE_SP', aon11_phasev0);