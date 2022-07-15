import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d
# epsilons = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.5, 2.0, 2.5, 3.0] # linear loss
epsilons = [0, 0.1, 0.3, 0.5, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.3, 1.5, 1.7, 2.0] # gaussian
# epsilons = [0, 1., 3., 4., 7., 8., 12.] # poisson

test_losses= [[-2.64669999,-4.03639149,-4.26486044,-4.99957578,-5.37519887,-5.70146694
,-5.91920665,-6.15615647,-6.365477,-6.62653392,-6.67416991,-6.67889521
,-6.79976225,-6.8843764,-6.91460551,-7.02307315,-7.03508449,-7.0616991
,-7.15982486,-7.10909208,-7.15005837,-7.23077156,-7.25872033,-7.24746902
,-7.26028791,-7.25809361,-7.24647437,-7.29827408,-7.28609576,-7.32396287
,-7.29969911,-7.28647703,-7.32286592,-7.32384072,-7.3255527,-7.34498358
,-7.32912318,-7.33044087,-7.34498358,-7.32296822]
,[-2.79324369,-3.82978129,-4.24897274,-4.92001915,-5.53992752,-5.81906574
,-5.8179279,-6.16466992,-6.5204587,-6.51675284,-6.61435392,-6.62825848
,-6.8605694,-6.90095352,-7.08662745,-6.92691976,-7.10778136,-7.10363816
,-7.10775976,-7.1325146,-7.1507611,-7.11753831,-7.2303856,-7.25888657
,-7.18147071,-7.2499219,-7.23700085,-7.30929296,-7.28804144,-7.30716245
,-7.3247826,-7.27699244,-7.31572071,-7.32210876,-7.31728643,-7.33957458
,-7.34498358,-7.30256627,-7.33895516,-7.34498358]
,[-2.6989311,-3.85806318,-4.41158894,-5.23851994,-5.53109666,-5.67811401
,-5.90839872,-6.10850537,-6.41308488,-6.58703019,-6.57697971,-6.72541022
,-6.66898029,-6.9624381,-6.97501282,-7.07356851,-7.10454946,-7.11619493
,-7.12087378,-7.16000265,-7.13986504,-7.19237091,-7.19057699,-7.29755518
,-7.24418324,-7.26795559,-7.24184909,-7.27880367,-7.32187741,-7.29892595
,-7.30737984,-7.31196592,-7.31162874,-7.34498358,-7.32400979,-7.32924972
,-7.33044087,-7.3366171,-7.32969477,-7.34498358]
,[-2.74618925,-3.77661022,-4.3783329,-5.11032836,-5.5501802,-5.81716046
,-5.79749666,-6.11697865,-6.22143283,-6.48117372,-6.77966974,-6.79260359
,-6.83464423,-6.84227332,-6.94519208,-6.96573863,-7.13143809,-7.10769375
,-7.18701243,-7.08184503,-7.19461169,-7.20313834,-7.19807204,-7.25112998
,-7.26732168,-7.29096013,-7.2255501,-7.24684819,-7.26207693,-7.29083625
,-7.27529713,-7.30265968,-7.30010047,-7.28671954,-7.33780276,-7.32567924
,-7.32036425,-7.32183237,-7.32986475,-7.33957458]
,[-2.52664932,-3.72404051,-4.33641112,-5.22236389,-5.48388988,-5.7733908
,-5.97579934,-6.34603242,-6.23152596,-6.49899345,-6.72311549,-6.74553991
,-6.81936929,-6.81962041,-6.96742438,-7.02988645,-7.00478469,-7.10439673
,-7.08636782,-7.11384174,-7.16262928,-7.20506924,-7.23767635,-7.27459814
,-7.23850356,-7.2798754,-7.29296398,-7.32843751,-7.30402999,-7.31227581
,-7.32065673,-7.29577665,-7.30926359,-7.32567924,-7.30049547,-7.33699011
,-7.34088531,-7.29572836,-7.33073286,-7.33083299]
,[-2.74425033,-3.50371551,-4.56380183,-5.08323329,-5.30766523,-6.00397017
,-5.9867583,-6.06477787,-6.35134732,-6.57883016,-6.6966878,-6.76897709
,-6.80245343,-6.91410777,-6.95423908,-6.90071578,-7.06375419,-7.14451344
,-7.13343995,-7.15599278,-7.14953714,-7.23285943,-7.27241279,-7.24883616
,-7.27692127,-7.28267145,-7.25708371,-7.25559615,-7.30852759,-7.29122031
,-7.32640259,-7.31981024,-7.28385146,-7.32683044,-7.33583323,-7.31962221
,-7.32303552,-7.3307322,-7.32273153,-7.34277671]
,[-2.75497742,-3.59306523,-4.51743359,-4.97007948,-5.65345501,-5.75142515
,-5.99876629,-6.25934664,-6.3104542,-6.50761815,-6.57891516,-6.78806545
,-6.79915576,-6.89430717,-6.9501741,-6.92593809,-6.99195935,-7.08599729
,-7.16403363,-7.18726555,-7.20603937,-7.24134297,-7.27815333,-7.23010019
,-7.21872598,-7.25075688,-7.30784637,-7.30991745,-7.3034602,-7.28838755
,-7.30509757,-7.32943261,-7.31383041,-7.32757751,-7.32957276,-7.32859835
,-7.31796731,-7.33196426,-7.33677956,-7.34451421]
,[-2.7330679,-3.65343788,-4.3148434,-4.98642493,-5.36377268,-5.684783
,-6.05866251,-6.15129784,-6.4034439,-6.48203449,-6.59709791,-6.76282631
,-6.84894046,-6.90189746,-6.96023454,-7.00853117,-7.08525322,-7.10586457
,-7.16978007,-7.17311203,-7.15884346,-7.26071428,-7.23849749,-7.26667172
,-7.25566287,-7.27870617,-7.24407167,-7.27033535,-7.30648798,-7.28904826
,-7.31040839,-7.32151573,-7.33785756,-7.32354434,-7.31843611,-7.31268353
,-7.34498358,-7.34377707,-7.33555864,-7.3361196,]
,[-2.86093112,-3.8078367,-4.4177834,-4.90964034,-5.54337427,-5.5880888
,-5.97128541,-6.01686847,-6.32328142,-6.59156837,-6.60387366,-6.67529358
,-6.79598776,-6.88714043,-6.83565185,-6.90011063,-7.0513175,-7.17104355
,-7.06238811,-7.17238597,-7.16053555,-7.20804905,-7.21790773,-7.22752007
,-7.26477949,-7.30682191,-7.2365664,-7.29010976,-7.31738263,-7.31360222
,-7.31174139,-7.31224199,-7.33388397,-7.30468804,-7.34327562,-7.31826926
,-7.30979758,-7.3349531,-7.31867537,-7.34413231]
,[-2.58426354,-3.76900555,-4.55005824,-4.99832034,-5.35383516,-5.90317173
,-6.13834219,-6.21374794,-6.43005713,-6.53006117,-6.56165663,-6.79112549
,-6.76424751,-6.85497688,-6.97942149,-6.96163049,-7.05837105,-7.11856593
,-7.05307981,-7.18407881,-7.20258226,-7.15956261,-7.24517597,-7.28104554
,-7.28094055,-7.3039892,-7.28844692,-7.31020338,-7.27575934,-7.31749596
,-7.31612877,-7.30679547,-7.31529054,-7.31882629,-7.30622683,-7.33459777
,-7.31385568,-7.309649,-7.33756623,-7.33860016]
,[-2.73088596,-3.76931916,-4.78364032,-4.92861975,-5.43665871,-5.56116923
,-5.9018319,-6.23039511,-6.40720347,-6.68457551,-6.75230841,-6.72613226
,-6.95164703,-6.90501759,-6.94646847,-6.98168986,-7.08286078,-7.09780442
,-7.1069209,-7.18888485,-7.16197073,-7.2221337,-7.19761494,-7.2308596
,-7.25363487,-7.20692152,-7.20566325,-7.30570158,-7.28891857,-7.29167764
,-7.28606652,-7.31038991,-7.32959867,-7.32384958,-7.34424672,-7.32622115
,-7.3253232,-7.32170342,-7.32560522,-7.34375769]
,[-3.24861819,-3.87883257,-4.43732493,-5.2503564,-5.31473277,-5.73489759
,-5.91211429,-6.25043018,-6.36809625,-6.52288644,-6.55116621,-6.70209136
,-6.8968891,-6.92682861,-6.99505478,-7.00003512,-7.027068,-7.10785367
,-7.1680652,-7.14534314,-7.17349024,-7.19874637,-7.20201878,-7.24047087
,-7.28591415,-7.23695271,-7.30619765,-7.29465903,-7.29956774,-7.30715844
,-7.27298553,-7.32118728,-7.31743218,-7.28615502,-7.32649033,-7.31294186
,-7.32460206,-7.32180201,-7.32606061,-7.33684061]
,[-2.75934925,-3.86188874,-4.5486201,-5.15078435,-5.44369059,-5.74660243
,-5.82838865,-5.96943794,-6.31913176,-6.43551948,-6.63872149,-6.68577613
,-6.84365838,-6.84048995,-6.93071603,-7.09458278,-7.05637814,-7.05460405
,-7.11757424,-7.15090456,-7.17365551,-7.237292,-7.18819481,-7.29082416
,-7.27851825,-7.28792079,-7.264226,-7.29404524,-7.26073342,-7.31543993
,-7.2773025,-7.31147741,-7.32489327,-7.32542031,-7.30841256,-7.3353805
,-7.3255527,-7.33430398,-7.33590616,-7.31110448]
,[-2.81493974,-3.83173475,-4.44753258,-4.95132022,-5.41756742,-5.71905173
,-5.93276487,-6.32867199,-6.30144135,-6.32430595,-6.59056105,-6.67568536
,-6.80667489,-6.90313804,-7.04675001,-6.92061557,-7.02795313,-7.04616958
,-7.15338149,-7.15484097,-7.1281847,-7.25053889,-7.25708096,-7.19126097
,-7.27517102,-7.27090036,-7.28209257,-7.27476611,-7.30173783,-7.29938493
,-7.28031262,-7.30300673,-7.29421498,-7.33282354,-7.33044021,-7.32388169
,-7.32093549,-7.33130197,-7.33905888,-7.33895516]
,[-2.48283089,-3.81310681,-4.46075053,-4.95918857,-5.21280768,-5.89549773
,-5.98372692,-6.16475179,-6.31626192,-6.56157182,-6.61029642,-6.61175827
,-6.75898777,-6.78818168,-6.89904443,-6.94539534,-7.10094804,-7.09012234
,-7.11486699,-7.16390375,-7.16319754,-7.23163249,-7.23951022,-7.21590102
,-7.22506337,-7.26105655,-7.25278058,-7.24330066,-7.30715359,-7.28958112
,-7.31872844,-7.30152183,-7.32921826,-7.31937641,-7.32087917,-7.31811206
,-7.32854569,-7.32977623,-7.32697685,-7.32631419]
,[-2.75026255,-3.72443625,-4.61843574,-4.9673035,-5.31256214,-5.8949283
,-5.83363231,-6.26139233,-6.36257591,-6.49440355,-6.6459378,-6.76983445
,-6.83590002,-6.7685592,-6.94505447,-6.98305969,-6.96604447,-7.05631446
,-7.09908031,-7.14235644,-7.19964009,-7.18153482,-7.24018535,-7.28434583
,-7.26505832,-7.24440118,-7.24467485,-7.28508137,-7.28092378,-7.31803906
,-7.31864389,-7.31255243,-7.32169491,-7.33104364,-7.33391841,-7.33409335
,-7.32480956,-7.32470552,-7.31946415,-7.33609198]
,[-2.80027706,-3.77270127,-4.56359588,-5.03199726,-5.36781893,-5.57693804
,-5.884964,-6.10827538,-6.20768864,-6.32500413,-6.52713587,-6.66845875
,-6.86631732,-6.90587553,-6.90617097,-7.04767452,-7.05671932,-7.01519982
,-7.10101145,-7.0953265,-7.14906864,-7.19985437,-7.20640818,-7.27668781
,-7.2586856,-7.25015786,-7.25333495,-7.24974354,-7.30375545,-7.30095064
,-7.30964835,-7.30290188,-7.30485221,-7.31071708,-7.31799601,-7.33404464
,-7.33082564,-7.33581945,-7.34013527,-7.33576175]]

TRAIN_SIZE = len(test_losses[0])
print(TRAIN_SIZE)
train_sizes = np.arange(1, TRAIN_SIZE+1)

plt.title("Linear Loss 7D Gaussian with FGM")
plt.xlabel("Size of Training Dataset")
plt.ylabel("Test Loss")
for i in range(len(epsilons)): # range(len(epsilons)):
    print('eps:', epsilons[i])
    ysmoothed = gaussian_filter1d(test_losses[i], sigma=2)
    plt.plot(train_sizes, ysmoothed, label=f"Ɛ = {epsilons[i]}")
plt.legend(loc="right")
plt.savefig(f"linear_gaussian_fgm_7d_all.png")
plt.clf()

"""
# 1
plt.title("Linear Regression Gaussian")
plt.xlabel("Size of Training Dataset")
plt.ylabel("Test Loss")
for i in [1,2,3]: # range(len(epsilons)):
    print('eps:', epsilons[i])
    plt.plot(train_sizes, test_losses[i], label=f"Ɛ = {epsilons[i]}")
plt.legend(loc="best")
plt.savefig(f"linreg_gaussian_fgsm_1d_weak.png")
plt.clf()

# 2
for i in [13, 14, 15, 16]:
    print('eps:', epsilons[i])
    plt.plot(train_sizes, test_losses[i], label=f"Ɛ = {epsilons[i]}")
plt.legend(loc="best")
plt.savefig(f"linreg_gaussian_fgsm_1d_strong.png")
"""