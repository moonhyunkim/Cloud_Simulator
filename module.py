"""
Cloud Simulator - Module

 • Author : Moonhyun kim
 • Date : May  , 2020
 • Last modified date : May 28, 2020

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


Order = [645, 439, 806, 593, 430, 725, 594, 410, 271, 340, 995, 158, 234, 652, 734, 803, 84, 285, 25, 260, 267, 587, 951, 385, 107, 841, 535, 77, 829, 154, 379, 356, 710, 334, 169, 920, 83, 213, 723, 459, 816, 967, 766, 13, 281, 501, 166, 840, 929, 997, 309, 16, 947, 435, 807, 329, 851, 917, 905, 256, 367, 749, 855, 404, 318, 904, 536, 5, 683, 778, 607, 238, 720, 194, 316, 109, 681, 792, 200, 145, 216, 940, 819, 273, 628, 793, 634, 206, 647, 398, 222, 279, 562, 959, 280, 954, 996, 615, 580, 266, 44, 612, 378, 1001, 175, 131, 274, 368, 784, 871, 307, 507, 92, 60, 568, 177, 133, 678, 640, 945, 137, 980, 389, 374, 686, 624, 774, 566, 953, 985, 891, 775, 629, 649, 162, 171, 6, 994, 301, 800, 205, 896, 43, 674, 761, 246, 21, 646, 74, 68, 685, 485, 132, 733, 809, 724, 901, 223, 897, 635, 878, 889, 921, 504, 344, 123, 722, 814, 579, 741, 37, 833, 426, 180, 942, 46, 528, 136, 794, 178, 193, 370, 561, 895, 126, 740, 152, 483, 464, 708, 595, 277, 89, 106, 207, 671, 342, 787, 890, 971, 549, 255, 248, 364, 702, 946, 682, 488, 446, 780, 15, 310, 462, 719, 357, 822, 348, 885, 688, 563, 912, 128, 7, 300, 440, 883, 930, 903, 65, 512, 186, 670, 764, 704, 656, 577, 846, 531, 706, 403, 428, 856, 892, 343, 713, 812, 91, 421, 955, 345, 854, 11, 738, 159, 783, 711, 355, 401, 293, 282, 821, 922, 505, 438, 759, 18, 977, 836, 906, 613, 427, 695, 810, 578, 161, 176, 958, 211, 539, 550, 592, 278, 543, 328, 663, 974, 71, 245, 598, 144, 408, 556, 494, 786, 676, 45, 405, 48, 869, 843, 313, 863, 135, 769, 371, 527, 650, 960, 326, 900, 298, 754, 478, 288, 532, 949, 553, 597, 956, 460, 576, 308, 564, 164, 1000, 730, 376, 914, 745, 1002, 35, 835, 716, 399, 231, 230, 661, 388, 943, 758, 253, 386, 156, 795, 642, 514, 751, 935, 58, 492, 81, 827, 813, 377, 801, 500, 881, 173, 113, 314, 852, 750, 397, 924, 32, 472, 620, 1003, 204, 352, 520, 823, 879, 444, 590, 70, 53, 873, 425, 100, 436, 913, 320, 936, 884, 516, 270, 768, 525, 452, 138, 63, 127, 515, 210, 306, 919, 705, 909, 850, 30, 251, 49, 217, 28, 547, 69, 110, 625, 353, 699, 653, 797, 284, 125, 215, 776, 659, 934, 90, 85, 489, 64, 157, 707, 148, 418, 962, 731, 697, 249, 630, 680, 975, 330, 406, 623, 969, 407, 4, 103, 621, 432, 80, 34, 118, 419, 927, 773, 1, 668, 672, 963, 508, 541, 296, 115, 24, 952, 455, 667, 268, 983, 382, 533, 139, 832, 22, 241, 486, 762, 534, 669, 50, 554, 170, 571, 40, 415, 537, 291, 641, 581, 888, 447, 831, 124, 95, 384, 717, 602, 728, 303, 496, 837, 202, 976, 467, 698, 684, 767, 790, 451, 120, 160, 87, 950, 391, 233, 658, 818, 72, 742, 254, 726, 471, 198, 327, 618, 362, 155, 57, 187, 286, 315, 545, 600, 119, 882, 165, 339, 604, 129, 311, 998, 524, 8, 861, 363, 197, 989, 802, 633, 506, 450, 351, 365, 332, 236, 687, 567, 54, 925, 968, 465, 798, 147, 785, 796, 693, 862, 721, 513, 225, 979, 319, 529, 933, 820, 972, 66, 97, 476, 441, 192, 188, 718, 826, 181, 844, 102, 732, 323, 559, 409, 938, 482, 474, 858, 261, 263, 825, 517, 560, 141, 167, 993, 739, 866, 195, 299, 79, 130, 865, 219, 360, 872, 381, 609, 86, 218, 224, 114, 143, 743, 737, 760, 149, 292, 214, 199, 341, 252, 396, 619, 981, 791, 712, 805, 290, 312, 777, 383, 655, 239, 42, 992, 59, 811, 78, 518, 849, 412, 799, 692, 944, 715, 98, 235, 237, 880, 876, 487, 19, 589, 61, 361, 324, 845, 838, 691, 984, 75, 709, 957, 573, 575, 574, 265, 454, 772, 591, 926, 639, 664, 380, 247, 424, 617, 565, 262, 937, 229, 456, 986, 354, 727, 638, 56, 497, 416, 902, 322, 104, 868, 596, 228, 400, 907, 272, 510, 153, 626, 966, 538, 196, 221, 747, 433, 458, 908, 867, 911, 336, 703, 1005, 1006, 453, 413, 606, 431, 830, 755, 570, 990, 302, 763, 781, 847, 569, 973, 185, 289, 584, 503, 67, 544, 603, 874, 183, 558, 41, 189, 116, 112, 894, 258, 632, 585, 402, 654, 675, 350, 121, 765, 540, 864, 448, 601, 321, 842, 484, 498, 437, 387, 519, 673, 555, 736, 468, 111, 789, 38, 491, 932, 390, 179, 62, 700, 611, 411, 479, 898, 232, 648, 73, 212, 26, 414, 373, 259, 746, 614, 10, 694, 657, 987, 331, 931, 714, 644, 887, 243, 445, 788, 463, 359, 52, 244, 99, 94, 916, 941, 970, 250, 393, 886, 859, 276, 651, 521, 226, 227, 511, 275, 346, 631, 220, 877, 240, 287, 305, 168, 696, 636, 395, 893, 14, 582, 17, 2, 690, 643, 82, 394, 542, 965, 988, 333, 105, 182, 804, 557, 203, 509, 853, 679, 523, 9, 939, 295, 860, 457, 146, 756, 283, 551, 923, 839, 964, 530, 748, 828, 163, 429, 502, 480, 599, 824, 20, 337, 469, 490, 51, 47, 875, 808, 588, 637, 150, 442, 108, 369, 76, 294, 665, 552, 572, 190, 608, 666, 915, 338, 610, 729, 548, 269, 392, 297, 347, 191, 605, 627, 3, 122, 36, 586, 470, 583, 948, 899, 771, 420, 443, 23, 526, 910, 257, 473, 817, 142, 349, 466, 834, 29, 662, 978, 134, 735, 616, 928, 660, 88, 982, 477, 31, 201, 33, 208, 779, 475, 335, 317, 848, 546, 961, 417, 325, 782, 499, 264, 461, 101, 434, 495, 304, 358, 815, 209, 117, 151, 12, 372, 423, 857, 93, 172, 481, 757, 752, 753, 918, 493, 422, 870, 999, 677, 1004, 174, 744, 770, 184, 96, 140, 27, 701, 55, 375, 366, 622, 449, 242, 991, 522, 39, 689]
schedule = [0, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 8, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 6, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 8, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 4, 7, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 2, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 1, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]

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
    
    def __init__ (self, Hname, Hnumber, Hcpu, Hram, Jnum, VM, TCU, TDU, STAT) :
        self.Host_name=Hname
        self.Host_number=Hnumber
        self.Host_CPUs = Hcpu
        self.Host_RAM = Hram
        self.Number_of_Job = Jnum
        self.VMs = VM
        self.Total_CPU_Usage = TCU
        self.Total_Disk_Usage = TDU
        self.Status = STAT 
    
    def print_Status (self): 
        print('\t{:<8} Number of Job : {:<4} Total CPU usage : {:<6} Total Disk Usage : {:<6} Status : {:<5} '.format(self.Host_name, self.Number_of_Job, self.Total_CPU_Usage, self.Total_Disk_Usage, self.Status))



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
    Host_list = []
    for i in range(1, number+1): 
        Host = new_Host('Host#'+str(i), i, 72, 400, 0 , [], 0.0, 0.0 , 'Activated')
        Host_list.append(Host)
    return Host_list



#원하는 개수만큼 가상머신 생성
def create_VM (number) :
    folder_path = 'usage_data2'
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
        Overload_host = sorted(Overload_host, key=lambda x : x.Total_CPU_Usage, reverse=True)
        while Overload_host :
            temp = Overload_host.pop(0)
            migration(temp,  Normal_host, Underload_host, Shutdown_host, vm_Selection, host_Selection, Run_VM, VM_list)
        print('---- [Done] \n')
        return 1

def migration_Underloadhost (Host_list, vm_Selection, host_Selection, Run_VM, VM_list) :
    print("     Start Migration (Underload Host)")
    Overload_host = []
    Normal_host = []
    Underload_host = []
    Shutdown_host = [] 
    for i in Host_list :
        if i.Status == "Overloaded" : Overload_host.append(i)
        elif i.Status == "Underloaded" : Underload_host.append(i)
        elif i.Status == "Normal" : Normal_host.append(i)
        else : Shutdown_host.append(i)

    if len(Underload_host) == 0 : 
        print("\t\tㄴ[No Action]")
        return 0 
        
    else :
        Underload_host = sorted(Underload_host, key=lambda x : x.Total_CPU_Usage)
        while Underload_host :
            temp = Underload_host.pop(0)
            migration(temp,  Normal_host, Underload_host, Shutdown_host, vm_Selection, host_Selection, Run_VM, VM_list)
        print('---- [Done] \n')
        return 1
###        time.sleep(1)

def migration(_from, to_normal, to_under, to_shutdown, vm_Selection, host_Selection, Run_VM, VM_list) :
    if vm_Selection == "random_choice" :
        queue_VM = [] 
        while True :
            if not _from.VMs : break
            else :  
                queue_VM.append(choice_VM.random_choice(_from)) #랜덤 VM추출
                update_Host_info(_from, VM_list, Run_VM) #오버로드, 언더로드 호스트 정보 업데이트
                if (_from.Total_CPU_Usage < 80 and _from.Total_CPU_Usage > 30) or _from.Total_CPU_Usage == 0.0 :
                    break                
        
        if host_Selection == "random_choice" :
            while queue_VM :
                target_host = 0
                temp_VM = queue_VM.pop(0)
                target_host = choice_Host.random_choice(temp_VM,to_normal,Run_VM)
                if target_host == 0 :
                   ## print(target_host)
                    if to_under :
                        print('언더에 하나 있음'+str(len(to_under)))
                        target_host = choice_Host.random_choice(temp_VM, to_under, Run_VM)
                        if target_host == 0 :
                            target_host = choice_Host.random_choice(temp_VM, to_shutdown, Run_VM)
                            print('\t '+target_host.Host_name+" is now activated")
                            global Number_of_Host_restart
                            Number_of_Host_restart +=1  
                            if target_host == 0 :
                                print('error')
                                break     
                    else :
                       ## print(target_host) 
                        target_host = choice_Host.random_choice(temp_VM, to_shutdown, Run_VM)
                        print('\t '+target_host.Host_name+" is now activated")
                        Number_of_Host_restart
                        Number_of_Host_restart +=1  
                        if target_host == 0 :
                            print('error')
                            break        
                target_host.VMs.append(temp_VM)
                global Number_of_migration 
                Number_of_migration += 1 
                update_Host_info(target_host, VM_list, Run_VM) #마이그레션된 호스트 정보 업데이트
                print('\t {:<7}\'s {:<8} is transferred to {:<5}'.format(_from.Host_name, temp_VM, target_host.Host_name))  




            
            

    else : 
        print("None")
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
    else :
        for j in Host.VMs :
            temp = find_VM_info(j, Run_VM)
            if temp.VM_exeTime == temp.VM_curTime :
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
    check_Host_Status(Host_list, Detect_Policy)
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
        if k.Status =="Normal" or k.Status =="Underload" : Activated_Host_list.append(k)
        else : Shutdown_Host_list.append(k)
    
    print('    Activated Host')
    for k in Activated_Host_list :
###        time.sleep(0.1)
        k.print_Status()
    print('    Shutdown Host')
    for k in Shutdown_Host_list :
###       time.sleep(0.1)
        k.print_Status()    


    return Host_list , Run_VM #시작을 위한 호스트 리스트 전달 
    








def executing_1Cycle (Host_list, VM_list, Run_VM, Queue_VM, schedule, Order, Detect_Policy, VM_Selection_Policy, Cycle) :
    print("---------------------------------------------------"+str(Cycle+1)+" Cycle---------------------------------------------------")
    global Total_running_time
    global Max_Activated 
    global CPU_SLAV_time 
    global Disk_SLAV_time

    Total_running_time += 1
    Activated = 0 
    Shutdown = 0


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
                i.print_Status()
            else :
                Shutdown += 1 
        print('Activated Host : {:<3}, Shutdown Host : {:<3}'.format(Activated, Shutdown))
        
        print('\n---- Check the Hosts status ...')    
        check_Host_Status(Host_list, Detect_Policy)
        print_HostList(Host_list)
        for i in Host_list : 
            if i.Total_CPU_Usage > 80 :
                CPU_SLAV_time += 1
            elif i.Total_Disk_Usage > 80 :
                Disk_SLAV_time +=1 


        if len(Run_VM) == 1 : 
            print('\n---- There isn\'t any new jobs,  ... Skip the migration') 
            print_current_status()
            
        else : 
            print('\n---- Start migration')
            flag1 = migration_Overloadhost(Host_list, "random_choice", "random_choice", Run_VM, VM_list)
            flag2 = migration_Underloadhost(Host_list, "random_choice", "random_choice", Run_VM, VM_list)

            if flag1+flag2 == 0 :
                print('\n---- Migration is not happened')
            else : 
                print('\n---- Stauts of Hosts After migration')
                Host_list = sorted(Host_list, key=lambda x : x.Host_number)
                for i in Host_list : 
                    update_Host_info(i,VM_list, Run_VM)
                    if i.Status != 'Shutdown' :
                        i.print_Status()
            print_current_status()



    else : 
        print('\n---- Current stauts of Hosts')
        for i in Host_list : 
            update_Host_info(i, VM_list, Run_VM)
            if i.Status != 'Shutdown' :
                Activated += 1 
                i.print_Status()
            else :
                Shutdown += 1 
        
        print('Activated Host : {:<3}, Shutdown Host : {:<3}'.format(Activated, Shutdown))
        print('\n---- Start Allocation')
        while Queue_VM : 
            shuffle(Host_list)
            temp = Queue_VM.pop(0)
            Run_VM.append(temp)
            for i in range(1,31):
                if Host_list[i-1].Status != 'Shutdown' :
                    Host_list[i-1].VMs.append(temp.VM_name)     
                    print('\t'+temp.VM_name+"\t is allocated to "+Host_list[i-1].Host_name)
                    for j in Host_list[i-1].VMs :
                        Host_list[i-1].Total_CPU_Usage += find_VM_CPU_usage(j, Run_VM)
                        Host_list[i-1].Total_Disk_Usage += find_VM_Disk_usage(j, Run_VM)
                        Host_list[i-1].Number_of_Job += 1
                    break
        
        print('\n---- Stauts of Hosts After allocation')
        Host_list = sorted(Host_list, key=lambda x : x.Host_number)
        for i in Host_list : 
            update_Host_info(i,VM_list, Run_VM)
            if i.Status != 'Shutdown' :
                i.print_Status()
        print('\n---- Check the Hosts status ...')    
        check_Host_Status(Host_list, Detect_Policy)
        print_HostList(Host_list)
        for i in Host_list : 
            if i.Total_CPU_Usage > 80 :
                CPU_SLAV_time += 1
            elif i.Total_Disk_Usage > 80 :
                Disk_SLAV_time +=1 


        print('\n---- Start migration')
        flag1 = migration_Overloadhost(Host_list, "random_choice", "random_choice", Run_VM, VM_list)
        flag2 = migration_Underloadhost(Host_list, "random_choice", "random_choice", Run_VM, VM_list)

        if flag1+flag2 == 0 :
            print('\n---- Migration is not happened')
        else : 
            print('\n---- Stauts of Hosts After migration')
            Host_list = sorted(Host_list, key=lambda x : x.Host_number)
            for i in Host_list : 
                update_Host_info(i,VM_list, Run_VM)
                if i.Status != 'Shutdown' :
                    i.print_Status()
        print_current_status()
        if Activated >= Max_Activated :
            Max_Activated = Activated


def print_current_status () :
    print('\n---- Results')
    print('\t Total running time : ' + str(Total_running_time))
    print('\t CPU SLAV time : ' + str(CPU_SLAV_time))
    print('\t Disk SLAV time : '+ str(Disk_SLAV_time))
    print('\t Max Activated Host : ' + str(Max_Activated))
    print('\t Number of migration : ' + str(Number_of_migration))
    print('\t Number of Host restart : '+str(Number_of_Host_restart))
    temp1 = round(CPU_SLAV_time/Total_running_time *100,2)
    temp2 = round(Disk_SLAV_time/Total_running_time * 100,2)
    print('\t CPU SLAV time per Active Host : '+str(temp1)+'%')
    print('\t DISK SLAV time per Active Host : '+str(temp2)+'%')
