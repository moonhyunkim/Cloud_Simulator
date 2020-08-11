"""
Cloud Simulator

 • Author : Moonhyun kim
 • Date : May 15 , 2020
 • Last modified date : Aug 5, 2020

 • Department of Computer Science at Chungbuk National University
"""

from random import randrange
from random import shuffle
import detect_Host
import choice_VM
import choice_Host
import time

##reulst
global CPU_SLAV_time
CPU_SLAV_time = 0.0
global Disk_SLAV_time 
Disk_SLAV_time = 0.0
global Number_of_migration
Number_of_migration = 0
global Number_of_Host_restart
Number_of_Host_restart = 0
global Total_running_time  
Total_running_time = 0.0 
global Max_Activated
Max_Activated = 0
global Total_Active_Time
Total_Active_Time = 0 
global Total_Energy_consumption
Total_Energy_consumption = 0.0
Total_Active_Time = 0 
global VMs 
VMs = 0 
global Hosts
Hosts = 0



Order = [446, 115, 175, 845, 75, 834, 350, 327, 100, 584, 160, 709, 535, 601, 733, 492, 263, 1111, 1019, 941, 1041, 208, 382, 1046, 965, 689, 974, 953, 595, 268, 922, 291, 167, 970, 898, 684, 235, 145, 915, 573, 431, 243, 438, 570, 652, 338, 625, 752, 850, 681, 555, 743, 1043, 634, 331, 614, 476, 84, 505, 41, 95, 46, 567, 844, 404, 516, 975, 917, 1033, 448, 276, 412, 449, 1060, 754, 571, 588, 1035, 837, 55, 785, 454, 293, 411, 972, 990, 920, 619,1133, 692, 200, 919, 450, 436, 280, 1098, 427, 12, 1091, 339, 315, 848, 767, 1004, 287, 1104, 1129, 463, 887, 218, 1123, 513, 1093, 305, 336, 611, 271, 353, 164, 1120, 501, 384, 297, 925, 679, 29, 97, 369, 907, 251, 217, 479, 518, 155, 405, 660, 275, 1068, 296, 644, 1062, 247, 880, 1009, 169, 914, 530, 883, 373, 493, 483, 607, 591, 758, 686, 564, 197, 216, 910, 394, 529, 298, 182, 83, 73, 274, 490, 808, 1045, 1119, 983, 87, 195, 137, 323, 672, 943, 895, 157, 540, 1036, 1039, 778, 526, 947, 811, 647, 651, 719, 360, 295, 4, 822, 599, 1047, 865, 685, 876, 1044, 775, 1006, 342, 1034, 11, 994, 255, 707, 655, 161, 864, 667, 549, 906, 27, 1029, 67, 489, 664, 724, 877, 938, 254, 1042, 45, 772, 726, 1090, 796, 703, 725, 1052, 345, 92, 583, 1070, 49, 730, 357, 991, 1075, 602, 871, 28, 442, 963, 205, 527, 38, 252, 650, 1021, 249, 514, 425, 632, 675, 979, 458, 22, 764, 128, 101, 517, 171, 424, 519, 533, 416, 206, 179, 633, 408, 349, 815, 544, 759, 316, 1, 626, 716, 301, 622, 696, 1055, 670, 245, 1076, 642, 1005, 849, 1072, 747, 24, 578, 1082, 417, 609, 241, 94, 230, 727, 542, 383, 1087, 978, 575, 847, 257, 1027, 713, 888, 802, 717, 398, 859, 289, 507, 279, 604, 648, 478, 1059, 904, 1083, 284, 996, 761, 608, 392, 396, 981, 737, 1080, 328, 1103, 358, 624, 869, 748, 1058, 399, 103, 885, 799, 183, 159, 893, 556, 958, 1048, 875, 56, 444, 987, 1130, 1079, 319, 143, 773, 498, 646, 148, 762, 226, 866, 389, 1096, 520, 905, 973, 935, 1089, 870, 385, 964, 1118, 470, 896, 531, 690, 123, 993, 998, 63, 173, 1011, 751, 166, 428, 90, 485, 572, 807, 715, 613, 201, 262, 820, 937, 9, 1110, 26, 999, 790, 72, 356, 310, 668, 188, 186, 326, 111, 1050, 185, 536, 114, 406, 951, 158, 795, 465, 130, 120, 163, 525, 379, 146, 51, 340, 219, 810, 563, 302, 223, 13, 443, 629, 6, 797, 623, 170, 456, 225, 332, 683, 663, 566, 671, 1128, 58, 631, 836, 698, 1018, 739, 1102, 388, 899, 420, 1016, 313, 593, 1100, 497, 441, 738, 177, 248, 375, 597, 253, 1092, 135, 841, 110, 308, 76, 1084, 682, 792, 374, 1014, 91, 872, 50, 3, 191, 551, 1028, 1007, 1054, 862, 1025, 1126, 1097, 962, 740, 706, 755, 397, 180, 794, 699, 1012, 300, 812, 481, 765, 1114, 657, 491, 294, 997, 65, 776, 393, 37, 61, 455, 627, 561, 1010, 318, 453, 511, 221, 495, 309, 562, 753, 466, 215, 1008, 736, 886, 710, 236, 838, 705, 653, 832, 39, 894, 1116, 68, 827, 901, 714, 277, 210, 32, 618, 314, 220, 757, 734, 678, 290, 637, 98, 842, 52, 88, 194, 126, 198, 312, 104, 673, 48, 119, 464, 430, 222, 53, 728, 1053, 770, 112, 43, 321, 524, 666, 480, 1051, 1088, 285, 1095, 532, 620, 484, 763, 113, 378, 403, 86, 723, 582, 93, 35, 656, 486, 352, 821, 125, 731, 558, 102, 433, 766, 8, 569, 127, 36, 523, 702, 924, 695, 7, 509, 852, 677, 636, 363, 606, 414, 81, 550, 371, 278, 85, 365, 57, 181, 944, 471, 380, 335, 213, 237, 329, 377, 154, 299, 429, 860, 14, 432, 460, 1108, 873, 418, 421, 760, 311, 581, 948, 1115, 955, 1023, 961, 711, 499, 435, 10, 474, 1015, 638, 1113, 506, 1125, 496, 172, 187, 330, 729, 782, 372, 367, 817, 47, 818, 814, 361, 687, 142, 982, 341, 281, 605, 579, 592, 1000, 17, 184, 988, 240, 641, 234, 732, 746, 701, 482, 868, 843, 18, 232, 21, 139, 1101, 333, 419, 635, 669, 122, 1109, 791, 30, 468, 162, 784, 343, 538, 209, 874, 1064, 500, 749, 598, 966, 168, 923, 643, 977, 165, 1032, 900, 1001, 995, 283, 212, 269, 781, 745, 1061, 813, 259, 929, 780, 512, 824, 117, 472, 439, 956, 565, 908, 659, 853, 840, 272, 190, 547, 586, 693, 697, 825, 793, 133, 193, 676, 522, 967, 413, 366, 1081, 829, 559, 603, 1117, 203, 744, 552, 930, 889, 149, 768, 931, 105, 1003, 742, 846, 933, 5, 121, 662, 239, 665, 451, 839, 344, 370, 927, 78, 487, 238, 1127, 960, 288, 691, 976, 347, 422, 459, 426, 718, 400, 835, 250, 1063, 774, 1065, 401, 70, 560, 942, 116, 878, 325, 932, 950, 882, 64, 440, 1017, 265, 957, 851, 936, 826, 211, 639, 928, 945, 854, 108, 151, 831, 152, 805, 362, 971, 861, 324, 771, 1121, 645, 348, 1086, 909, 303, 568, 364, 1066, 787, 1040, 934, 940, 574, 74, 42, 541, 351, 617, 788, 548, 1105, 15, 286, 452, 136, 610, 902, 543, 261, 674, 224, 1107, 949, 415, 337, 1030, 640, 1085, 69, 368, 554, 2, 407, 1057, 590, 477, 1122, 816, 346, 153, 1073, 654, 918, 150, 447, 1077, 1078, 750, 735, 1020, 242, 307, 916, 402, 721, 144, 264, 355, 107, 445, 521, 229, 1124, 1112, 40, 576, 1056, 830, 704, 99, 266, 256, 34, 969, 410, 630, 779, 423, 577, 954, 890, 134, 196, 594, 959, 798, 946, 809, 952, 246, 694, 628, 199, 783, 658, 44, 457, 756, 1013, 828, 863, 857, 174, 1049, 1038, 260, 508, 304, 833, 510, 176, 585, 178, 557, 71, 1002, 494, 258, 1026, 589, 1074, 921, 553, 317, 897, 462, 131, 545, 741, 528, 434, 819, 20, 1022, 616, 539, 1132, 292, 804, 786, 912, 621, 891, 270, 1094, 204, 534, 395, 354, 1106, 596, 984, 855, 911, 473, 856, 777, 31, 54, 992, 320, 1037, 147, 381, 467, 700, 141, 989, 892, 228, 720, 661, 409, 214, 66, 267, 806, 580, 60, 680, 233, 391, 386, 227, 77, 1067, 546, 19, 89, 390, 156, 722, 79, 502, 801, 649, 867, 387, 23, 1099, 475, 469, 968, 823, 769, 688, 140, 612, 503, 800, 16, 129, 192, 437, 884, 207, 980, 803, 985, 59, 1069, 80, 124, 1131, 913, 488, 202, 461, 879, 132, 376, 939, 600, 82, 138, 587, 903, 62, 106, 1071, 712, 789, 189, 96, 359, 537, 334, 282, 858, 881, 118, 33, 306, 244, 273, 986, 1024, 25, 615, 1031, 231, 109, 515, 322, 504, 926, 708]
schedule = [0, 0, 0, 4, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 8, 0, 0, 2, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 9, 0, 0, 6, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 7, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 2, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 8, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 9, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 8, 3, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 8, 0, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 5, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 5, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 1, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 8, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 3, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 2, 0, 0, 0, 0, 0, 0, 0]
#호스트 클래스 
class new_Host :
    Host_name = ''
    Host_number = 0
    Host_CPUs = 72
    Host_RAM = 400
    Number_of_Job = 0
    VMs = []
    Total_CPU_Usage = 0.0
    Total_Disk_Usage = 0.0
    Status = ''
    Total_Activated_time = 0.0
    FLAG = 0 # 0,1
    TIME = 0
    Usage = []
    Energy_comsumption = 0.0
    
    def __init__ (self, Hname, Hnumber, Hcpu, Hram, Jnum, VM, TCU, TDU, STAT, ATVT, FLAG=0, TIME=0 ) :
        self.Host_name=Hname
        self.Host_number=Hnumber
        self.Host_CPUs = Hcpu
        self.Host_RAM = Hram
        self.Number_of_Job = Jnum
        self.VMs = VM
        self.Total_CPU_Usage = TCU
        self.Total_Disk_Utsage = TDU
        self.Status = STAT 
        self.Total_Activated_time = ATVT
        self.Usage = []
        self.Energy_comsumption = 0.0 

    def print_Status (self): 
        print('\t{:<8} Number of Job : {:<4} Total CPU usage : {:<6} Total Disk Usage : {:<6} FLAG : {:<2} TIME : {:<4} Status : {:<5} '.format(self.Host_name, self.Number_of_Job, round(self.Total_CPU_Usage,2), round(self.Total_Disk_Usage,2), self.FLAG, self.TIME ,self.Status))



#VM 클래스
class new_VM : 
    VM_name = ''
    VM_number = 0 
    VM_usage = []
    VM_curTime = 0
    VM_exeTime = 0
    VM_slavTime = 0

    def __init__ (self, Vname, Vnumber, Vusage, cTime, eTime, slavTime) : 
        self.VM_name = Vname
        self.VM_number = Vnumber
        self.VM_usage = Vusage
        self.VM_curTime = cTime
        self.VM_exeTime = eTime 
        self.VM_slavTime = slavTime



#원하는 개수만큼 호스트 생성
def create_Host(number) :
    global Hosts 
    Hosts = number
    Host_list = []
    for i in range(1, number+1): 
        Host = new_Host('Host#'+str(i), i, 72, 400, 0 , [], 0.0, 0.0 , 'Activated', 1.0)
        Host_list.append(Host)
    return Host_list



#원하는 개수만큼 가상머신 생성
def create_VM (number) :
    global VMs
    VMs = number
    folder_path = 'Usage_data/usage_data1'#####폴더 패스
    VM_list = []
    for i in range(1, number+1) :
        f = open(folder_path+'/data'+str(i)+'.txt')
        usage_data = f.readlines()
        VM = new_VM('VM#'+str(i), i, usage_data, 0, len(usage_data), 0)
        VM_list.append(VM)
    return VM_list



#Host 출력
def print_HostList (Host_list) : 
    temp = []
    print("\tOverloaded host : ", end='')
    for i in Host_list :
        if i.Status == 'Overloaded' :
            temp.append(i.Host_name)
    if not temp : 
        print("None")
    else : 
        for i in temp :
            if i == temp[-1] :
                print(i)
            else :
                print(i , end=', ')

    temp = []
    print("\tUnderloaded Host : ", end='')
    for i in Host_list :
        if i.Status == 'Underloaded' :
            temp.append(i.Host_name)
    if not temp : 
        print("None")
    else : 
        for i in temp :
            if i == temp[-1] :
                print(i)
            else :
                print(i , end=', ')


    
#VM의 CPU 사용량 찾기
def find_VM_CPU_usage (VM_name, Run_VM) :
    VM_CPU_usage=0.0
    #VM_number = int(VM_name.replace("VM#",''))
    for i in Run_VM : 
        if i.VM_name == VM_name : 
            VM_CPU_usage += float(i.VM_usage[i.VM_curTime].split(' ')[1]) 
            break
    return VM_CPU_usage


#VM의 Disk 사용량 찾기
def find_VM_Disk_usage (VM_name, Run_VM) :
    VM_Disk_usage=0.0
    #VM_number = int(VM_name.replace("VM#",''))
    for i in Run_VM : 
        if i.VM_name == VM_name :
            VM_Disk_usage += float(i.VM_usage[i.VM_curTime].split(' ')[3])
            break
    return VM_Disk_usage


#Overload, Underload 탐지
def check_Host_Status (Host_list, Detect_Policy) :
    #1.Static_threshold Policy  
    if Detect_Policy == 'static_threshold' :
        return detect_Host.static_threshold(Host_list)
    else : 
        print('Select Detect_Policy')
        return 0
        
        
#VM 마이그레이션 진행
def migrate_VMs(Overload_host, Normal_Host, Underload_host, VM_Selection_Policy) :
    if not Overload_host : 
        print('Overload Host is not detected')
        return 

    #overloaded --> Normal Host
    #   VM selection (Random, High Utilization,,)
    #   Host selection (Host Selection)
    #   if normal host is full, then migration to Extra_Host(underloaded Host)
    #   Update Run_VM, Queue_VM, Host_list(change status)
    # 


#실행될 VM list 대기열 이동 
#def pop_VMs (Vm_list, Queue_VM, schedule) :
    # first, pop vm_number from order_list following Schdule
    # extract number --> check order_list
    # find VM+number in VM list 


#호스트 변경사항 저장   
#def update_Host() 

#VM 정보 찾기
def find_VM_info(VM_name, Run_VM) : 
    for i in Run_VM :
        if i.VM_name == VM_name :
            return i




def migration_Overloadhost (Host_list, vm_Selection, host_Selection, Run_VM, VM_list) :
    print("     Start Migration (Overload Host)")
    Overload_host = []
    Normal_host = []
    Underload_host = []
    Shutdown_host = [] 
    for i in Host_list :
        if i.Status == "Overloaded" : Overload_host.append(i)
        elif i.Status == "Underloaded" : Underload_host.append(i)
        elif i.Status == "Normal" : Normal_host.append(i)
        else : Shutdown_host.append(i)

    if len(Overload_host) == 0 : 
        print("\t\tㄴ[No Action]")
        return 0
        
    else :
        # Overload_host = sorted(Overload_host, key=lambda x : x.Total_CPU_Usage, reverse=True)
        # while Overload_host :
        #     temp = Overload_host.pop(0)
        #     migration(temp,  Normal_host, Underload_host, Shutdown_host, vm_Selection, host_Selection, Run_VM, VM_list)
        # print('---- [Done] \n')
        # return 1
        numberer = 0 
        while True :
            Overload_host = []
            Normal_host = []
            Underload_host = []
            Shutdown_host = [] 
            for i in Host_list :
                if i.Status == "Overloaded" : Overload_host.append(i)
                elif i.Status == "Underloaded" : Underload_host.append(i)
                elif i.Status == "Normal" : Normal_host.append(i)
                else : Shutdown_host.append(i)
                        
            if Overload_host : 
                temp = Overload_host.pop(0)
                migration(temp,  Normal_host, Underload_host, Shutdown_host, vm_Selection, host_Selection, Run_VM, VM_list)
                if not Overload_host: break
            else : break
        print('---- [Done] \n')
        return 1
        
def migration_Underloadhost (Host_list, vm_Selection, host_Selection, Run_VM, VM_list) :
    global Number_of_Host_restart
    print("     Start Migration (Underload Host)")
    Overload_host = []
    Normal_host = []
    Underload_host = []
    Shutdown_host = [] 
    for i in Host_list :
        if i.Status == "Overloaded" : Overload_host.append(i)
        elif i.Status == "Underloaded" and i.FLAG == 0  : Underload_host.append(i)
        elif i.Status == "Normal" : Normal_host.append(i)
        else : Shutdown_host.append(i)

    if len(Underload_host) == 0 : 
        print("\t\tㄴ[No Action]")
        return 0 
    elif len(Underload_host) == 1 and len(Normal_host) == 0 :
        print("\t\t ㄴThere's only one Host, [No Action]")
        return 0
    else :
        while True :
            Overload_host = []
            Normal_host = []
            Underload_host = []
            Shutdown_host = [] 
            for i in Host_list :
                if i.Status == "Overloaded" : Overload_host.append(i)
                elif i.Status == "Underloaded" and i.FLAG == 0 : Underload_host.append(i)
                elif i.Status == "Normal" : Normal_host.append(i)
                else : Shutdown_host.append(i)

            if Underload_host : 
                shuffle(Underload_host)
                temp = Underload_host.pop(0)
                migration(temp,  Normal_host, Underload_host, Shutdown_host, vm_Selection, host_Selection, Run_VM, VM_list)
                if not Underload_host: break
            else : break
        print('---- [Done] \n')
        return 1

def migration(_from, to_normal, to_under, to_shutdown, vm_Selection, host_Selection, Run_VM, VM_list) :
    queue_VM = [] 
    while True :
        if not _from.VMs : break
        else :  
            statement = 'queue_VM.append(choice_VM.'+vm_Selection+'(_from, Run_VM))' #마이그레이션 할 VM추출
            eval(statement)
            update_Host_info(_from, VM_list, Run_VM) #오버로드, 언더로드 호스트 정보 업데이트
            if (_from.Total_CPU_Usage < 80 and _from.Total_CPU_Usage > 20) or _from.Total_CPU_Usage == 0.0 :
                break
    
    while queue_VM :
        list_sum = to_normal + to_under + to_shutdown 
        to_normal , to_under , to_shutdown = [], [], []
        for i in list_sum :
            if i.Status == "Normal" :
                to_normal.append(i)
            elif i.Status == "Underloaded" :
                to_under.append(i)
            elif i.Status == "Shutdown" :
                to_shutdown.append(i)
        
        for i in to_normal :
            if i.Status != 'Normal' :
                print(i.Status , i.Host_name)
                time.sleep(5)
        for i in to_under :
            if i.Status != 'Underloaded' :
                print(i.Status , i.Host_name)
                time.sleep(5)
        for i in to_shutdown :
            if i.Status != 'Shutdown' :
                print(i.Status , i.Host_name)
                time.sleep(5)

        target_host = 0
        temp_VM = queue_VM.pop(0)
        statement = 'choice_Host.'+host_Selection+'(temp_VM,to_normal,Run_VM)'
        target_host = eval(statement)
        if target_host == 0 :
            ## print(target_host)
            if to_under :
                statement = 'choice_Host.'+host_Selection+'(temp_VM,to_under,Run_VM)'
                target_host = eval(statement)
                if target_host == 0 :
                    statement = 'choice_Host.'+host_Selection+'(temp_VM,to_shutdown,Run_VM)'
                    target_host = eval(statement)
                    if target_host == 0 :
                        print('error')
                        time.sleep(10)
                        break     
            else :
               #for i in to_shutdown :
                #    print(i.Host_name,i.Total_CPU_Usage,i.Status)
                #print('stop')
                statement = 'choice_Host.'+host_Selection+'(temp_VM,to_shutdown,Run_VM)'
                target_host = eval(statement)
                if target_host == 0 :
                    print('error1')
                    time.sleep(10)
                    break        
        target_host.VMs.append(temp_VM)
        global Number_of_migration 
        Number_of_migration += 1 
        update_Host_info(target_host, VM_list, Run_VM) #마이그레션된 호스트 정보 업데이트
        if target_host.Status == 'Underloaded' :
            target_host.Status = 'Underloaded yet'#임시방편
        print('\t{:<7}\'s {:<8} is transferred to {:<5}'.format(_from.Host_name, temp_VM, target_host.Host_name))  


'''   
def migration(_from, _to, vm_Selection, Run_VM) :
    if vm_Selection == "random_choice" :
        while len(_from) != 0 :
            temp = _from.pop(0)
            while len(temp.VMs) != 0 :
                temp_VM = choice_VM.random_choice(temp) #VM랜덤 초이스
                for i in _to :
                    if i.Total_CPU_Usage + find_VM_CPU_usage(temp_VM, Run_VM) <= 80.0 :
                        i.VMs.append(temp_VM)
                        update_Host_info(i, Run_VM)
                        time.sleep(0.1)
                        print('\t {:<7}\'s {:<8} is transffered to {:<5}'.format(temp.Host_name, temp_VM, i.Host_name))
                        break
'''



def update_Host_info (Host, VM_list, Run_VM) :
    Host.Total_CPU_Usage = 0.0
    Host.Total_Disk_Usage = 0.0
    Host.Number_of_Job = 0
    temp_list=[]
    if not Host.VMs :
        Host.Status = "Shutdown"
        Host.FLAG = 0
        Host.TIME = 0 
    else :
        for j in Host.VMs :
            temp = find_VM_info(j, Run_VM)
            if temp.VM_exeTime <= temp.VM_curTime :
                temp_list.append(j)
            else :
                Host.Total_CPU_Usage += find_VM_CPU_usage(j, Run_VM)
                Host.Total_Disk_Usage += find_VM_Disk_usage(j, Run_VM)
                Host.Number_of_Job += 1    
    for i in temp_list :
        Host.VMs.remove(i)
        Run_VM.remove(find_VM_info(i,Run_VM))
    Host.Total_CPU_Usage = round(Host.Total_CPU_Usage,2)
    Host.Total_Disk_Usage = round(Host.Total_Disk_Usage,2)
    detect_Host.static_threshold([Host])

#Order에 따른 VM 추출
def find_VM_Number (VM_list, Order) :
    temp = Order.pop(0)
    for i in range(0, len(VM_list)) :
        if VM_list[i].VM_number == temp :
            return i
    print("Can't Find")

    
#시물레이션을 위한 초기화 (Host에 VM할당 // Overload, Underload 탐지)
def initialize (Host_list, VM_list, Run_VM, Order, Detect_Policy, VM_Selection_Policy) :
    Activated_Host_list = []
    Shutdown_Host_list = []
    
    print('---- [3] Allocate VM to Host')
###    time.sleep(0.5)
    for i in range(1,31) :
        Run_VM.append(VM_list.pop(find_VM_Number(VM_list, Order)))
        #Run_VM.append(VM_list.pop(VM_list.index(list(item for item in VM_list if item['index']==random_value)[0])))
        Host_list[i-1].VMs.append(Run_VM[i-1].VM_name)                         #호스트 리스트가 0부터 시작하기 때문에 -1
        print('\t'+Run_VM[i-1].VM_name+"\t is allocated to "+Host_list[i-1].Host_name)
        for j in Host_list[i-1].VMs :
            Host_list[i-1].Total_CPU_Usage += find_VM_CPU_usage(j, Run_VM)
            Host_list[i-1].Total_Disk_Usage += find_VM_Disk_usage(j, Run_VM)
            Host_list[i-1].Number_of_Job += 1

###        time.sleep(0.1)
    print('---- [1][2][3] Done \n')
###    time.sleep(0.5) 
    print('---- Host Status (After initial Migration)')
    Host_list = sorted(Host_list, key=lambda x : x.Host_number)
    for i in Host_list :
        i.print_Status()


    #부하 탐지 함수 호출
    print('\n---- [4] Check the Host\'s status ...')
    check_Host_Status(Host_list, Detect_Policy[0])
###    time.sleep(1)
    print_HostList(Host_list)
    print('---- Done \n')
###    time.sleep(1)
    
    #초기 마이그레이션진행
    print('---- [5] Start migration')
    migration_Overloadhost(Host_list, "random_choice", "random_choice", Run_VM, VM_list)
    migration_Underloadhost(Host_list, "random_choice", "random_choice", Run_VM, VM_list)
    
    print('---- Host Status (After initial Migration)')
    Host_list = sorted(Host_list, key=lambda x : x.Host_number)
    for k in Host_list :
        if k.Status != 'Shutdown': Activated_Host_list.append(k)
        else : Shutdown_Host_list.append(k)
    
    print('    Activated Host')
    for k in Activated_Host_list :
###     time.sleep(0.1)
        k.print_Status()
    print('    Shutdown Host')
    for k in Shutdown_Host_list :
###     time.sleep(0.1)
        k.print_Status()    
    return Host_list , Run_VM #시작을 위한 호스트 리스트 전달 
    








def executing_1Cycle (Host_list, VM_list, Run_VM, Queue_VM, schedule, Order, Detect_Policy, VM_Selection_Policy, Host_Selection_Policy, Cycle) :
    for i in Host_list : 
        if i.Status == 'Shutdown' :
            pass 
        else : 
            i.Energy_comsumption +=round((111 + (111*i.Total_CPU_Usage/100)*0.5 + (111*i.Total_Disk_Usage/100)*0.1) /3600, 5)

    print("---------------------------------------------------"+str(Cycle+1)+" Cycle---------------------------------------------------")
    global Total_running_time
    global Max_Activated 
    global CPU_SLAV_time 
    global Disk_SLAV_time
    global Number_of_Host_restart
    min_time = 35
    # 변경사항
    VMSP = VM_Selection_Policy[1]  # 0:random , 1: High_CPU_Usage 2: MMT 
    HSP = Host_Selection_Policy[3] # 0:random , 1:Low_cpu  2:Low_CPUDISK  3:MMEHS
    

    Total_running_time += 1
    Activated = 0 
    Shutdown = 0
    
    for i in Host_list :
        if i.Status != 'Shutdown' :
            i.Total_Activated_time += 1.0



    #시점 증가
    for k in Run_VM :
        k.VM_curTime += 1 
    if schedule :
        new_Job = schedule.pop(0)   #새로 들어오는 작업의 개수
        print(str(new_Job)+" job(\'s) is submitted")
    else : 
        new_Job = 0
        print(str(new_Job)+" job(\'s) is submitted")

    #작업 개수만큼 Queue로 이동
    while new_Job != 0 :
        Queue_VM.append(VM_list[find_VM_Number(VM_list,Order)])
        new_Job -= 1 
    
    if len(Queue_VM) == 0 :
        print('\n---- Current stauts of Hosts')
        Host_list = sorted(Host_list, key=lambda x : x.Host_number)
        for i in Host_list : 
            update_Host_info(i, VM_list, Run_VM)

            if i.Status != 'Shutdown' :
                Activated += 1 
                i.TIME += 1
                i.print_Status()
            else :
                Shutdown += 1 
       
        for i in range(0,len(Host_list)) : 
            if Host_list[i].Status == 'Shutdown' :
                Host_list[i].Usage = []
            else :
                Host_list[i].Usage.append(Host_list[i].Total_CPU_Usage)
            

        print('Activated Host : {:<3}, Shutdown Host : {:<3}'.format(Activated, Shutdown))
        if Activated >= Max_Activated :
            Max_Activated = Activated
        print('\n---- Check the Hosts status ...')    
        check_Host_Status(Host_list, Detect_Policy[0])
        print_HostList(Host_list)
        for i in Host_list : 
            if i.Total_CPU_Usage > 80 :
                CPU_SLAV_time += 1
            elif i.Total_Disk_Usage > 80 :
                Disk_SLAV_time +=1 

        
        
        if len(Run_VM) == 0 : 
            print('\n---- There isn\'t any new jobs, [DONE]') 
            print_current_status(Host_list)
            
        else : 
            print('\n---- Start migration')
            flag1 = 0
            flag2 = 0
            over = 0
            under = 0
            for i in Host_list :
                if i.Total_CPU_Usage > 80 : 
                    over += 1
                elif i.Total_CPU_Usage <20 and i.Total_CPU_Usage != 0.0 : 
                    under +=1 
            
            if over >= 1 :   flag1 = migration_Overloadhost(Host_list, VMSP, HSP, Run_VM, VM_list)
            if under >= 1 : flag2 = migration_Underloadhost(Host_list, VMSP, HSP, Run_VM, VM_list)
            for i in Host_list :
                if i.FLAG == 1 and i.TIME >= min_time :
                    i.FLAG = 0

            if flag1+flag2 == 0 :
                print('\n---- Migration is not happened')
            else : 
                print('\n---- Stauts of Hosts After migration')
                Host_list = sorted(Host_list, key=lambda x : x.Host_number)
                for i in Host_list : 
                    update_Host_info(i,VM_list, Run_VM)
                    if i.Status != 'Shutdown' :
                        i.print_Status()


    else : 
        print('\n---- Current stauts of Hosts')
        for i in Host_list : 
            update_Host_info(i, VM_list, Run_VM)
            if i.Status != 'Shutdown' :
                Activated += 1 
                i.TIME += 1
                i.print_Status()
            else :
                Shutdown += 1 
        
        print('Activated Host : {:<3}, Shutdown Host : {:<3}'.format(Activated, Shutdown))
        print('\n---- Start Allocation')
        while Queue_VM : 
            temp = Queue_VM.pop(0)
            Run_VM.append(temp)
            statement = 'choice_Host.'+HSP+'(temp.VM_name, Host_list, Run_VM)'
            target_host = eval(statement)
            target_host.VMs.append(temp.VM_name)
            print('\t'+temp.VM_name+"\t is allocated to "+target_host.Host_name)
            target_host.Number_of_Job = 0
            target_host.Total_CPU_Usage = 0.0
            target_host.Total_Disk_Usage = 0.0
            for i in target_host.VMs :
                    target_host.Total_CPU_Usage += find_VM_CPU_usage(i, Run_VM)
                    target_host.Total_Disk_Usage += find_VM_Disk_usage(i, Run_VM)
                    target_host.Number_of_Job += 1
            
        
        for i in Host_list :
            if i.FLAG == 1 and i.TIME >= min_time :
                i.FLAG = 0

        # for i in Host_list : # flag, time 변화 테스트용
        #     if i.FLAG == 1 and i.Status!= 'Shutdown' :
        #         print(i.TIME)
        
            # for i in range(1,50):
            #     Host_list[i-1].VMs.append(temp.VM_name)     
            #     print('\t'+temp.VM_name+"\t is allocated to "+Host_list[i-1].Host_name)
            #     for j in Host_list[i-1].VMs :
            #         Host_list[i-1].Total_CPU_Usage += find_VM_CPU_usage(j, Run_VM)
            #         Host_list[i-1].Total_Disk_Usage += find_VM_Disk_usage(j, Run_VM)
            #         Host_list[i-1].Number_of_Job += 1
            #     break
        
        print('\n---- Stauts of Hosts After allocation')
        Host_list = sorted(Host_list, key=lambda x : x.Host_number)
        for i in Host_list : 
            update_Host_info(i,VM_list, Run_VM)
            if i.Status != 'Shutdown' :
                i.print_Status()

                
        print('\n---- Check the Hosts status ...')   
        check_Host_Status(Host_list, Detect_Policy[0])
        print_HostList(Host_list)
        for i in Host_list : 
            if i.Total_CPU_Usage > 80 :
                CPU_SLAV_time += 1
            elif i.Total_Disk_Usage > 80 :
                Disk_SLAV_time +=1 
        ###time.sleep(10)
        
        print('\n---- Start migration')
        flag1 = 0
        flag2 = 0
        over = 0
        under = 0
        for i in Host_list : 
            if i.Total_CPU_Usage > 80 : 
                over += 1
            elif i.Total_CPU_Usage <20 and i.Total_CPU_Usage != 0.0 : 
                under +=1 
        
        if over >= 1 :   flag1 = migration_Overloadhost(Host_list, VMSP, HSP, Run_VM, VM_list)
        if under >= 1 : flag2 = migration_Underloadhost(Host_list, VMSP, HSP, Run_VM, VM_list)

        if flag1+flag2 == 0 :
            print('\n---- Migration is not happened')
        else : 
            print('\n---- Status of Hosts After migration')
            Host_list = sorted(Host_list, key=lambda x : x.Host_number)
            for i in Host_list : 
                update_Host_info(i,VM_list, Run_VM)
                if i.Status != 'Shutdown' :
                    i.print_Status()
        if not Run_VM:
            print_current_status(Host_list)

def update_Host_flag_time (Host_list, Run_VM) :
    for i in Host_list :
        if i.Status != 'Shutdown' and i.FLAG != 1 :
            i.TIME += 1
            



def print_current_status (Host_list) :
    global Total_Active_Time
    global Total_Energy_consumption
    for i in Host_list :
        Total_Active_Time+=i.Total_Activated_time
    print('\n---- Results')
    print('\t Number of Hosts : '+ str(Hosts))
    print('\t Number of VMs : '+ str(VMs))
    print('\t Total running time : ' + str(Total_running_time)+' sec')
    print('\t Total Host Activated Time : '+str(Total_Active_Time)+'sec')
    for i in Host_list :
        Total_Energy_consumption += i.Energy_comsumption
        Total_Energy_consumption += (1.15 * 111)/3600 * Number_of_Host_restart
    print('\t Max Activated Host : ' + str(Max_Activated))
    print('\t Number of CPU SLAV : ' + str(CPU_SLAV_time))
    print('\t Number of Disk SLAV : '+ str(Disk_SLAV_time))
    print('\t Number of migration : ' + str(Number_of_migration))
    print('\t Number of Host restart : '+str(Number_of_Host_restart))
    temp1 = round(CPU_SLAV_time/Total_Active_Time *100,5)
    temp2 = round(Disk_SLAV_time/Total_Active_Time * 100,5)
    print('\t CPU SLAV time per Active Host : '+str(temp1)+'%')
    print('\t DISK SLAV time per Active Host : '+str(temp2)+'%')
    print('\t Total Total Energy consumption : '+str(round(Total_Energy_consumption,3))+'kWh')
