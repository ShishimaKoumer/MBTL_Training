import cfg_ml
cfg = cfg_ml
P_info = cfg.P_info

###########################################################################
# 各種アドレス
###########################################################################
TIMER_AD = 0x59BA34
TR_FLAG_AD = 0x713700
DAMAGE_AD = 0x7144A0
HOSEI_AD = DAMAGE_AD - 12
UKEMI_AD = DAMAGE_AD - 4  # 受け身不能時間補正
CAM_AD = 0x714D80

STOP_AD = 0x72BA68
START_POSI_AD = 0x730D98
MAX_Damage_Pointer_AD = 0x731144

PLR_STRUCT_SIZE = 0xC14  # 3084

DAT_P1_AD = 0xB42EB0   # 1Pデータ開始位置
DAT_P2_AD = DAT_P1_AD + PLR_STRUCT_SIZE  # 2Pデータ開始位置
DAT_P3_AD = DAT_P2_AD + PLR_STRUCT_SIZE
DAT_P4_AD = DAT_P3_AD + PLR_STRUCT_SIZE

X_P1_AD = DAT_P1_AD + 0x64
X_P2_AD = X_P1_AD + PLR_STRUCT_SIZE
X_P3_AD = X_P2_AD + PLR_STRUCT_SIZE
X_P4_AD = X_P3_AD + PLR_STRUCT_SIZE

P_info[0].motion_type_ad = DAT_P1_AD + 0x40
P_info[1].motion_type_ad = DAT_P1_AD + 0x40 + PLR_STRUCT_SIZE
P_info[2].motion_type_ad = DAT_P1_AD + 0x40 + PLR_STRUCT_SIZE * 2
P_info[3].motion_type_ad = DAT_P1_AD + 0x40 + PLR_STRUCT_SIZE * 3

P_info[0].atk_ad = DAT_P1_AD + 0x60
P_info[1].atk_ad = DAT_P1_AD + 0x60 + PLR_STRUCT_SIZE
P_info[2].atk_ad = DAT_P1_AD + 0x60 + PLR_STRUCT_SIZE * 2
P_info[3].atk_ad = DAT_P1_AD + 0x60 + PLR_STRUCT_SIZE * 3

P_info[0].inv_ad = DAT_P1_AD + 0x61
P_info[1].inv_ad = DAT_P1_AD + 0x61 + PLR_STRUCT_SIZE
P_info[2].inv_ad = DAT_P1_AD + 0x61 + PLR_STRUCT_SIZE * 2
P_info[3].inv_ad = DAT_P1_AD + 0x61 + PLR_STRUCT_SIZE * 3

P_info[0].x_ad = DAT_P1_AD + 0x64
P_info[1].x_ad = DAT_P1_AD + 0x64 + PLR_STRUCT_SIZE
P_info[2].x_ad = DAT_P1_AD + 0x64 + PLR_STRUCT_SIZE * 2
P_info[3].x_ad = DAT_P1_AD + 0x64 + PLR_STRUCT_SIZE * 3

P_info[0].gauge_ad = DAT_P1_AD + 0xA0
P_info[1].gauge_ad = DAT_P1_AD + 0xA0 + PLR_STRUCT_SIZE
P_info[2].gauge_ad = DAT_P1_AD + 0xA0 + PLR_STRUCT_SIZE * 2
P_info[3].gauge_ad = DAT_P1_AD + 0xA0 + PLR_STRUCT_SIZE * 3

P_info[0].tag_flag_ad = DAT_P1_AD + 0x2A4
P_info[1].tag_flag_ad = DAT_P1_AD + 0x2A4 + PLR_STRUCT_SIZE
P_info[2].tag_flag_ad = DAT_P1_AD + 0x2A4 + PLR_STRUCT_SIZE * 2
P_info[3].tag_flag_ad = DAT_P1_AD + 0x2A4 + PLR_STRUCT_SIZE * 3

P_info[0].hitstop_ad = DAT_P1_AD + 0x296
P_info[1].hitstop_ad = DAT_P1_AD + 0x296 + PLR_STRUCT_SIZE
P_info[2].hitstop_ad = DAT_P1_AD + 0x296 + PLR_STRUCT_SIZE * 2
P_info[3].hitstop_ad = DAT_P1_AD + 0x296 + PLR_STRUCT_SIZE * 3

P_info[0].seeld_ad = DAT_P1_AD + 0x2A0
P_info[1].seeld_ad = DAT_P1_AD + 0x2A0 + PLR_STRUCT_SIZE
P_info[2].seeld_ad = DAT_P1_AD + 0x2A0 + PLR_STRUCT_SIZE * 2
P_info[3].seeld_ad = DAT_P1_AD + 0x2A0 + PLR_STRUCT_SIZE * 3

P_info[0].step_inv_ad = DAT_P1_AD + 0x2B8
P_info[1].step_inv_ad = DAT_P1_AD + 0x2B8 + PLR_STRUCT_SIZE
P_info[2].step_inv_ad = DAT_P1_AD + 0x2B8 + PLR_STRUCT_SIZE * 2
P_info[3].step_inv_ad = DAT_P1_AD + 0x2B8 + PLR_STRUCT_SIZE * 3

P_info[0].hit_ad = DAT_P1_AD + 0x2D8
P_info[1].hit_ad = DAT_P1_AD + 0x2D8 + PLR_STRUCT_SIZE
P_info[2].hit_ad = DAT_P1_AD + 0x2D8 + PLR_STRUCT_SIZE * 2
P_info[3].hit_ad = DAT_P1_AD + 0x2D8 + PLR_STRUCT_SIZE * 3

P_info[0].ukemi1_ad = DAT_P1_AD + 0x2DC
P_info[1].ukemi1_ad = DAT_P1_AD + 0x2DC + PLR_STRUCT_SIZE
P_info[2].ukemi1_ad = DAT_P1_AD + 0x2DC + PLR_STRUCT_SIZE * 2
P_info[3].ukemi1_ad = DAT_P1_AD + 0x2DC + PLR_STRUCT_SIZE * 3

P_info[0].ukemi2_ad = DAT_P1_AD + 0x2E4
P_info[1].ukemi2_ad = DAT_P1_AD + 0x2E4 + PLR_STRUCT_SIZE
P_info[2].ukemi2_ad = DAT_P1_AD + 0x2E4 + PLR_STRUCT_SIZE * 2
P_info[3].ukemi2_ad = DAT_P1_AD + 0x2E4 + PLR_STRUCT_SIZE * 3

P_info[0].motion_ad = DAT_P1_AD + 0x548
P_info[1].motion_ad = DAT_P1_AD + 0x548 + PLR_STRUCT_SIZE
P_info[2].motion_ad = DAT_P1_AD + 0x548 + PLR_STRUCT_SIZE * 2
P_info[3].motion_ad = DAT_P1_AD + 0x548 + PLR_STRUCT_SIZE * 3

P_info[0].anten_stop_ad = DAT_P1_AD + 0x731
P_info[1].anten_stop_ad = DAT_P1_AD + 0x731 + PLR_STRUCT_SIZE
P_info[2].anten_stop_ad = DAT_P1_AD + 0x731 + PLR_STRUCT_SIZE * 2
P_info[3].anten_stop_ad = DAT_P1_AD + 0x731 + PLR_STRUCT_SIZE * 3

P_info[0].moon_st_ad = DAT_P1_AD + 0x924
P_info[1].moon_st_ad = DAT_P1_AD + 0x924 + PLR_STRUCT_SIZE
P_info[2].moon_st_ad = DAT_P1_AD + 0x924 + PLR_STRUCT_SIZE * 2
P_info[3].moon_st_ad = DAT_P1_AD + 0x924 + PLR_STRUCT_SIZE * 3

P_info[0].moon_ad = DAT_P1_AD + 0x928
P_info[1].moon_ad = DAT_P1_AD + 0x928 + PLR_STRUCT_SIZE
P_info[2].moon_ad = DAT_P1_AD + 0x928 + PLR_STRUCT_SIZE * 2
P_info[3].moon_ad = DAT_P1_AD + 0x928 + PLR_STRUCT_SIZE * 3

P_info[0].noguard_ad = DAT_P1_AD + 0xB7C
P_info[1].noguard_ad = DAT_P1_AD + 0xB7C + PLR_STRUCT_SIZE
P_info[2].noguard_ad = DAT_P1_AD + 0xB7C + PLR_STRUCT_SIZE * 2
P_info[3].noguard_ad = DAT_P1_AD + 0xB7C + PLR_STRUCT_SIZE * 3
