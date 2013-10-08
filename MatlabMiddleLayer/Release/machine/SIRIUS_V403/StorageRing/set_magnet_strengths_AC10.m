% set_magnet_strengths_V403_AC10
% ==============================
% 2013-04-25 Ximenes

if strcmpi(mode_version,'AC10_1')
    %% ac10_1    (antigo moga_191)
    %%% QUADRUPOLOS
    %  ===========
    
    qaf_strength   =  2.537149508081614;
    qad_strength   = -2.72913396292989;
    qf1_strength   =  2.371935660488307;
    qf2_strength   =  3.352382329901055;
    qf3_strength   =  3.061721689600176;
    qf4_strength   =  2.726572517947555;
    
    qbd2_strength  = -3.956471221376155;
    qbf_strength   =  3.910851993130583;
    qbd1_strength  = -2.980215320655289;
    
    
    %%% SEXTUPOLOS
    %  ==========
    
    sa2_strength   =   52.72380076806903/2;
    sa1_strength   =  -143.8844478200684/2;
    sd1_strength   = -417.235066899276/2;
    sf1_strength   =  366.7874776704998/2;
    sd2_strength   =  -65.72359519210869/2;
    sd3_strength   = -258.2261103894817/2;
    sf2_strength   =  306.7833526228504/2;
    
    sb1_strength   =  -184.6185552543126/2;
    sb2_strength   =   97.98683543332642/2;


%% ac10_2 (antigo moga328)
elseif strcmpi(mode_version,'AC10_2')
    %%% QUADRUPOLOS
    %  ===========
    
    qaf_strength   =  2.537296184268377;
    qad_strength   = -2.73415324178606;
    qf1_strength   =  2.371727588481388;
    qf2_strength   =  3.353138936660851;
    qf3_strength   =  3.062693827255291;
    qf4_strength   =  2.72911516713545;
    
    qbd2_strength  = -3.954309719796702;
    qbf_strength   =  3.910203239069909;
    qbd1_strength  = -2.99072488074151;
    
    %%% SEXTUPOLOS
    %  ==========
    
    sa2_strength   =    25.873;
    sa1_strength   =   -65.972;
    sd1_strength   =  -181.89875;
    sf1_strength   =   190.221;
    sd2_strength   =  -60.293;
    sd3_strength   =  -133.453;
    sf2_strength   =   150.920;
    
    sb1_strength   =  -96.6447;
    sb2_strength   =   50.622;


%% ac10_3 (eh o ac10_2 simetrizado em relacao ao BC)
elseif strcmpi(mode_version,'AC10_3')

    %%% QUADRUPOLOS
    %  ===========
    
    qaf_strength   =  2.540801;
    qad_strength   = -2.744679;
    qf1_strength   =  2.371977;
    qf2_strength   =  3.353143;
    qf3_strength   =  3.062984;
    qf4_strength   =  2.729574;
    
    qbd2_strength  = -3.966318;
    qbf_strength   =  3.908091;
    qbd1_strength  = -2.974256;
    
    %%% SEXTUPOLOS
    %  ==========
    
%     sa2_strength   =    25.873;
%     sa1_strength   =   -65.972;
%     sd1_strength   =  -182.338526;
%     sf1_strength   =   190.196570;
%     sd2_strength   =  -60.293;
%     sd3_strength   =  -133.453;
%     sf2_strength   =   150.920;
%     
%     sb1_strength   =  -96.6447;
%     sb2_strength   =   50.622;
    sa1_strength       =   -60.0563;
    sa2_strength       =    27.4663;
    sb1_strength       =  -102.4798;
    sb2_strength       =    59.9428;
    sd2_strength       =   -81.1457;
    sd3_strength       =  -146.8153;
    sf2_strength       =   154.3260;
    sd1_strength       =  -155.0830;
    sf1_strength       =   191.5520;

%% Antigo Moga0473modif-0512
% Um pouco de historia: esse modo eh o resultado de duas otimizacoes do
% MOGA. Primeiro, otimizei usando o ac10_3 como ponto inicial e peguei o
% resultado 0473. Mas esse resultado tinha uma sintonia vertical muito
% proxima do inteiro, entao aumentei a sintonia com o OPA e usei o
% resultado como ponto inicial para outra otimizacao, mas coloquei um
% vinculo adicional de que as sintonias deveriam ser maiores que 0.12.
% Peguei o resultado 0512 dessa simulacao e vi que ele melhorava tanto o
% tempo de vida, como a abertura dinamica, quando simulado com o conjunto
% padrao de erros, no tracy3.
%
elseif strcmpi(mode_version,'AC10_4')
    %%% QUADRUPOLOS
    %  ===========
    
    qaf_strength       =  2.53733156985179;
    qad_strength       = -2.729928269122092;
    qbd2_strength      = -3.960473342625189;
    qbf_strength       =  3.902662679038675;
    qbd1_strength      = -2.9676529175558;
    qf1_strength       =  2.368979188452946;
    qf2_strength       =  3.354162681362089;
    qf3_strength       =  3.080099756299886;
    qf4_strength       =  2.708484971587339;
    %%% SEXTUPOLOS
    %  ==========
    sa1_strength       = -123.1722496509632/2;
    sa2_strength       =   49.93065558027325/2;
    sb1_strength       = -221.8397738651525/2;
    sb2_strength       =  114.7544273034517/2;
    sd1_strength       = -346.6761204672601/2;
    sf1_strength       =  374.2717343204316/2;
    sd2_strength       = -129.7749377447802/2;
    sd3_strength       = -278.7913650216647/2;
    sf2_strength       =  317.433316097233/2;



%% Antigo Moga1139-2388
% Um pouco de historia: Rodamos o v403_ac10_4-Moga e obtivemos o resultado 1139.
% Com esse resultado como ponto inicial rodamos o v403_moga1139 e obtivemos o
% resultado 2388. Quando comparamos os dois com o ensemble de erros no
% tracy3 optamos pelo 2388.
elseif strcmpi(mode_version,'AC10_5')
    %%% QUADRUPOLOS
    %  ===========
    qaf_strength       =  2.53696119948142;
    qad_strength       = -2.729804812331968;
    qbd2_strength      = -3.960473342625189;
    qbf_strength       =  3.902662679038675;
    qbd1_strength      = -2.9676529175558;
    qf1_strength       =  2.367868077341835;
    qf2_strength       =  3.353792310991718;
    qf3_strength       =  3.079729385929515;
    qf4_strength       =  2.708114601216968;
    

    %%% SEXTUPOLOS
    %  ==========
    sa1_strength       = -115.7829759411277/2;
    sa2_strength       =   49.50386128829739/2;
    sb1_strength       = -214.5386552515188/2;
    sb2_strength       =  133.1252391065637/2;
    sd1_strength       = -302.6188062085843/2;
    sf1_strength       =  369.5045185071228/2;
    sd2_strength       = -164.3042864671946/2;
    sd3_strength       = -289.9270429064217/2;
    sf2_strength       =  333.7039740852999/2;




%% Testes de otimizacao de injecao 02/10/2013
% Apos Montar o script que simula a injecao no anel, notamos que estavamos
% com problemas para injetar tanto com os 4kickers, como com o pmm.
%  - O problema com os 4kickers eh que na segunda volta o feixe estava batendo
%  no septum, entao tinhamos que aumentar a sintonia da maquina e/ou mudar
%  o tuneshift com a amplitude, de forma que a oscilacao do feixe injetado
%  (altas amplitudes) seja mais rapida.
%  - O problema com o pmm eh que nosso espaco de fase horizontal tem um
%  bico muito apertado em angulo no lado negativo de x enquanto o feixe
%  injetado, devido ao kick do pmm, tem uma abertura muito grande, entao
%  devemos tentar aumentar a abertura angular ali (virar a coxinha)

elseif strcmpi(mode_version,'test_inject_4k')

%tentativa de aumentar tune com opa: 1ra
%     %%% QUADRUPOLOS
%     %  =========== (quads obtidos com o opa)
%     qaf_strength       = 2.536961 ;
%     qad_strength       = -2.729805;
%     qbd2_strength      = -3.960473;
%     qbf_strength       = 3.902663 ;
%     qbd1_strength      = -2.967653;
%     qf1_strength       = 2.357389 ;
%     qf2_strength       = 3.363276 ;
%     qf3_strength       = 3.079729 ;
%     qf4_strength       = 2.713552 ;
%     
%     
%     %%% SEXTUPOLOS
%     %  ========== (obtidos com o script do matlab)
%     % boa solucao para injecao 4k
%     sa1_strength       =  -58.9405;
%     sa2_strength       =   25.1813;
%     sb1_strength       = -107.7365;
%     sb2_strength       =   65.8960;
%     sd1_strength       = -155.8518;
%     sf1_strength       =  186.8334;
%     sd2_strength       = -80.1791;
%     sd3_strength       = -143.6776;
%     sf2_strength       =  162.9090;
    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%tentativa de aumentar tune com opa mantendo os mesmos sexts: 2da
%     %%% QUADRUPOLOS
%     %  =========== (quads obtidos com o opa)
%     qaf_strength       = 2.536961 ;
%     qad_strength       = -2.729805;
%     qbd2_strength      = -3.960473;
%     qbf_strength       = 3.902663 ;
%     qbd1_strength      = -2.967653;
%     qf1_strength       = 2.357389 ;
%     qf2_strength       = 3.363276 ;
%     qf3_strength       = 3.079729 ;
%     qf4_strength       = 2.713552 ;
%     
%     
%     %%% SEXTUPOLOS
%     %  ========== (os mesmos do AC10_5)
%     sa1_strength       = -115.7829759411277/2;
%     sa2_strength       =   49.50386128829739/2;
%     sb1_strength       = -214.5386552515188/2;
%     sb2_strength       =  133.1252391065637/2;
%     sd1_strength       = -302.6188062085843/2;
%     sf1_strength       =  369.5045185071228/2;
%     sd2_strength       = -164.3042864671946/2;
%     sd3_strength       = -289.9270429064217/2;
%     sf2_strength       =  333.7039740852999/2;
    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%tentativa mudar o tuneshift com amplitude mexendo so os sexts: 3ra
    %%% QUADRUPOLOS
    %  =========== (os mesmos do AC10_5)
    qaf_strength       =  2.53696119948142;
    qad_strength       = -2.729804812331968;
    qbd2_strength      = -3.960473342625189;
    qbf_strength       =  3.902662679038675;
    qbd1_strength      = -2.9676529175558;
    qf1_strength       =  2.367868077341835;
    qf2_strength       =  3.353792310991718;
    qf3_strength       =  3.079729385929515;
    qf4_strength       =  2.708114601216968;
    
    
    %%% SEXTUPOLOS
    %  ========== (obtidos com o script do matlab)
    % boa solucao para injecao 4k
    sa1_strength       =  -58.9405;
    sa2_strength       =   25.1813;
    sb1_strength       = -107.7365;
    sb2_strength       =   65.8960;
    sd1_strength       = -155.8518;
    sf1_strength       =  186.8334;
    sd2_strength       = -80.1791;
    sd3_strength       = -143.6776;
    sf2_strength       =  162.9090;
    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% outra boa solucao para injecao 4k, mas essa muda muito o tune shift com a
% amplitude, tomar cuidado.
%     sa1_strength       =   -57.1952;
%     sa2_strength       =    22.1193;
%     sb1_strength       =  -116.6017;
%     sb2_strength       =    62.2259;
%     sd2_strength       =   -92.1350;
%     sd3_strength       =  -148.5110;
%     sf2_strength       =   167.4148;
%     sd1_strength       =  -141.7308;
%     sf1_strength       =   186.9690;
    

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% boa solucao com o script de otimizacao do espaco de fase
% mas parece que a abertura dinamica nao esta muito boa
%     %%% QUADRUPOLOS
%     %  =========== (os mesmos do AC10_5)
%     qaf_strength       =  2.53696119948142;
%     qad_strength       = -2.729804812331968;
%     qbd2_strength      = -3.960473342625189;
%     qbf_strength       =  3.902662679038675;
%     qbd1_strength      = -2.9676529175558;
%     qf1_strength       =  2.367868077341835;
%     qf2_strength       =  3.353792310991718;
%     qf3_strength       =  3.079729385929515;
%     qf4_strength       =  2.708114601216968;
% 
% 
%     
%     %%% SEXTUPOLOS
%     %  ========== (obtidos com o script do matlab)
%     sa1_strength       =  -67.6329;
%     sa2_strength       =   18.4370;
%     sb1_strength       = -130.5790;
%     sb2_strength       =   59.2409;
%     sd1_strength       = -152.4642;
%     sf1_strength       =  184.3618;
%     sd2_strength       =  -85.2405;
%     sd3_strength       = -139.4236;
%     sf2_strength       =  169.3679;


elseif strcmpi(mode_version,'test_inject_pmm')
    
%lncc_v403_ac10_5-invcox_000093   
    %%% QUADRUPOLOS
    %  ===========
        qaf_strength       =  2.53696119948142 ;
        qad_strength       = -2.729804812331968;
        qbd2_strength      = -3.960473342625189;
        qbf_strength       =  3.902662679038675;
        qbd1_strength      = -2.9676529175558  ;
        qf1_strength       =  2.367868077341835;
        qf2_strength       =  3.353792310991718;
        qf3_strength       =  3.079729385929515;
        qf4_strength       =  2.708114601216968;
    
    
    %%% SEXTUPOLOS
    %  ==========
        sa1_strength       =-113.1981086610908/2;
        sa2_strength       = 35.41992724561523/2;
        sb1_strength       =-258.5626331672489/2;
        sb2_strength       = 123.0625698276054/2;
        sd1_strength       =-286.9408026023277/2;
        sf1_strength       = 334.4933257290978/2;
        sd2_strength       =-145.9794373625645/2;
        sd3_strength       =-328.864644424823 /2;
        sf2_strength       = 396.3103030055146/2;
  
 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% primeira tentativa real de virar a coxinha

%     %%% QUADRUPOLOS
%     %  =========== (mesmos quads do AC10_5)
%     qaf_strength       =  2.53696119948142;
%     qad_strength       = -2.729804812331968;
%     qbd2_strength      = -3.960473342625189;
%     qbf_strength       =  3.902662679038675;
%     qbd1_strength      = -2.9676529175558;
%     qf1_strength       =  2.367868077341835;
%     qf2_strength       =  3.353792310991718;
%     qf3_strength       =  3.079729385929515;
%     qf4_strength       =  2.708114601216968;
% 
% 
%     %%% SEXTUPOLOS
% %      ==========
%     sa1_strength       =   -60.2392;
%     sa2_strength       =    19.5175;
%     sb1_strength       =  -134.9419;
%     sb2_strength       =    62.0093;
%     sd2_strength       =   -83.8803;
%     sd3_strength       =  -171.3067;
%     sf2_strength       =   203.2820;
%     sd1_strength       =  -130.4733;
%     sf1_strength       =   167.3688;
    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%lncc_v403_ac10_5-Moga_000858

%      %%% QUADRUPOLOS
%      %  ===========
%     qaf_strength       = 2.537658457662712 ;
%     qad_strength       = -2.737004985263078;
%     qbd2_strength      = -3.957685119288232;
%     qbf_strength       = 3.904570491969777 ;
%     qbd1_strength      = -2.97399429698993 ;
%     qf1_strength       = 2.364973307077406 ;
%     qf2_strength       = 3.355983567160624 ;
%     qf3_strength       = 3.079012939179151 ;
%     qf4_strength       = 2.707699693838884 ;
% 
% 
%     %%% SEXTUPOLOS
% %      ==========
%     sa1_strength       = -121.8770703095287/2;
%     sa2_strength       = 46.75922686210009 /2;
%     sb1_strength       = -229.2424942716568/2;
%     sb2_strength       = 122.1875937851297 /2;
%     sd1_strength       = -304.7041246102518/2;
%     sf1_strength       = 358.3225430665879 /2;
%     sd2_strength       = -157.3890464079509/2;
%     sd3_strength       = -291.3442333179376/2;
%     sf2_strength       = 353.0546937179435 /2;

else
    error('Mode_version not implemented');
end






















%Testes
%% 403_ac10_4-Moga: resultado 1139
%     %%% QUADRUPOLOS
%     %  ===========
%     
%     qaf_strength       =  2.536129607255627;
%     qad_strength       = -2.72639768187918;
%     qbd2_strength      = -3.960219626878903;
%     qbf_strength       =  3.902885901652044;
%     qbd1_strength      = -2.967332427114794;
%     qf1_strength       =  2.368879224965777;
%     qf2_strength       =  3.353939502196436;
%     qf3_strength       =  3.079243799613321;
%     qf4_strength       =  2.707916311301111;
%     %%% SEXTUPOLOS
%     %  ==========
%     sa1_strength       = -121.6204530035251/2;
%     sa2_strength       =   50.34137075945026/2;
%     sb1_strength       = -214.7091208067262/2;
%     sb2_strength       =  130.4364776803027/2;
%     sd1_strength       = -311.0008132083819/2;
%     sf1_strength       =  369.7114975143294/2;
%     sd2_strength       = -156.3977076588722/2;
%     sd3_strength       = -289.191091356093/2;
%     sf2_strength       =  330.8038807650062/2;
   
    %% 403_ac10_4-Moga: resultado 0885
%     %%% QUADRUPOLOS
%     %  ===========
%     
%     qaf_strength       =  2.537439972497168;
%     qad_strength       = -2.729488049220083;
%     qbd2_strength      = -3.960347817209897;
%     qbf_strength       =  3.902566697903313;
%     qbd1_strength      = -2.967446322849456;
%     qf1_strength       =  2.369139260611449;
%     qf2_strength       =  3.354084940414377;
%     qf3_strength       =  3.08025523819532;
%     qf4_strength       =  2.708510885236575;
%     %%% SEXTUPOLOS
%     %  ==========
%     sa1_strength       = -118.3444338731154/2;
%     sa2_strength       =   47.34424134771261/2;
%     sb1_strength       = -214.4848531926572/2;
%     sb2_strength       =  118.2212285225685/2;
%     sd1_strength       = -313.2196020658923/2;
%     sf1_strength       =  368.6045807077905/2;
%     sd2_strength       = -156.6543073364475/2;
%     sd3_strength       = -284.0256064840537/2;
%     sf2_strength       =  332.4412625973211/2;

    %% 403_moga1139: resultado 0424
%     %%% QUADRUPOLOS
%     %  ===========
%     
%     qaf_strength       =  2.536618410493951;
%     qad_strength       = -2.730498796608363;
%     qbd2_strength      = -3.960482800715857;
%     qbf_strength       =  3.902455204986204;
%     qbd1_strength      = -2.967712338736793;
%     qf1_strength       =  2.367695501608838;
%     qf2_strength       =  3.35387741761896;
%     qf3_strength       =  3.079671860685185;
%     qf4_strength       =  2.707600830615592;
%     %%% SEXTUPOLOS
%     %  ==========
%     sa1_strength       = -120.2743539417698/2;
%     sa2_strength       =   46.70787975011622/2;
%     sb1_strength       = -216.8170631454972/2;
%     sb2_strength       =  131.3806720295649/2;
%     sd1_strength       = -307.1673848682601/2;
%     sf1_strength       =  366.2310728287079/2;
%     sd2_strength       = -158.9333638613506/2;
%     sd3_strength       = -289.1740717618469/2;
%     sf2_strength       =  338.266260916636/2;