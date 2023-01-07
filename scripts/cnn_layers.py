
# ====================================================================
#  You can add more layer shapes by creating new cnn_layers variables
# ====================================================================
# W, H, C, N, M, S, R, Wpad, Hpad, Wstride, Hstride



# ---------- BELOW ARE THE PROVIDED SHAPES (CONV LAYERS of 3 DNN Models) --------------------
# Alex Net w/o grouping specified in http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture9.pdf
# W, H, C, N, M, S, R, Wpad, Hpad, Wstride, Hstride
# cnn_layers = [
#     (227, 227, 3, 1, 96, 11, 11, 1, 1, 4, 4),
#     (27, 27, 96, 1, 256, 5, 5, 2, 2, 1, 1),
#     (13, 13, 256, 1, 384, 3, 3, 1, 1, 1, 1),
#     (13, 13, 384, 1, 384, 3, 3, 1, 1, 1, 1),
#     (13, 13, 384, 1, 256, 3, 3, 1, 1, 1, 1),
#     ]
# W, H, C, N, M, S, R, Wpad, Hpad, Wstride, Hstride
cnn_layers = [
    # W, H, C, N, M, S, R, Wpad, Hpad, Wstride, Hstride
    (80, 60, 1, 1, 64, 3, 3, 1, 1, 1, 1), # conv1a
    (80, 60, 64, 1, 64, 3, 3, 1, 1, 1, 1), # conv1b
    (80, 60, 64, 1, 64, 3, 3, 1, 1, 1, 1), # conv2a
    (80, 60, 64, 1, 64, 3, 3, 1, 1, 1, 1), # conv2b
    (80, 60, 64, 1, 128, 3, 3, 1, 1, 1, 1), # conv3a
    (80, 60, 128, 1, 128, 3, 3, 1, 1, 1, 1), # conv3b
    (80, 60, 128, 1, 128, 3, 3, 1, 1, 1, 1), # conv4a
    (80, 60, 128, 1, 128, 3, 3, 1, 1, 1, 1), # conv4b
    (80, 60, 128, 1, 256, 3, 3, 1, 1, 1, 1), # convPa
    (80, 60, 256, 1, 65, 1, 1, 0, 0, 1, 1), # convPb
    (80, 60, 256, 1, 256, 1, 1, 0, 0, 1, 1), # convDb
    ]

def op_size_calculator(layer:tuple):
    """
    layer:a tuple of length 11. W, H, C, N, M, S, R, Wpad, Hpad, Wstride, Hstride 
    """
    # W, H, C, N, M, S, R, Wpad, Hpad, Wstride, Hstride
    if len(layer)!=11:
        print("invalid input size")
        return 0
    W, H, C, N, M, S, R, Wpad, Hpad, Wstride, Hstride = layer
    Q = int((W - S + 2 * Wpad) / Wstride) + 1
    P = int((H - R + 2 * Hpad) / Hstride) + 1
    return (Q , P)
# VGG-1 Net Specified in [Shafiee, ISCA 2016]
# W, H, C, N, M, S, R, Wpad, Hpad, Wstride, Hstride
# cnn_layers = [
#     (224, 224, 3, 1, 64, 3, 3, 1, 1, 1, 1),
#     (112, 112, 64, 1, 128, 3, 3, 1, 1, 1, 1),
#     (56, 56, 128, 1, 256, 3, 3, 1, 1, 1, 1),
#     (56, 56, 256, 1, 256, 3, 3, 1, 1, 1, 1),
#     (28, 28, 256, 1, 512, 3, 3, 1, 1, 1, 1),
#     (28, 28, 512, 1, 512, 3, 3, 1, 1, 1, 1),
#     (14, 14, 512, 1, 512, 3, 3, 1, 1, 1, 1),
#     (14, 14, 512, 1, 512, 3, 3, 1, 1, 1, 1),
#     ]

# VGG-2 Net Specified in [Shafiee, ISCA 2016]
# W, H, C, N, M, S, R, Wpad, Hpad, Wstride, Hstride
# cnn_layers = [
#     (224, 224, 3, 1, 64, 3, 3, 1, 1, 1, 1),
#     (224, 224, 64, 1, 64, 3, 3, 1, 1, 1, 1),
#     (112, 112, 64, 1, 128, 3, 3, 1, 1, 1, 1),
#     (112, 112, 128, 1, 128, 3, 3, 1, 1, 1, 1),
#     (56, 56, 128, 1, 256, 3, 3, 1, 1, 1, 1),
#     (56, 56, 256, 1, 256, 3, 3, 1, 1, 1, 1),
#     (56, 56, 256, 1, 256, 1, 1, 0, 0, 1, 1),
#     (28, 28, 256, 1, 512, 3, 3, 1, 1, 1, 1),
#     (28, 28, 512, 1, 512, 3, 3, 1, 1, 1, 1),
#     (28, 28, 512, 1, 512, 1, 1, 0, 0, 1, 1),
#     (14, 14, 512, 1, 512, 3, 3, 1, 1, 1, 1),
#     (14, 14, 512, 1, 512, 3, 3, 1, 1, 1, 1),
#     (14, 14, 512, 1, 256, 1, 1, 1, 1, 1, 1),
#     ]
if __name__ == "__main__":
    print(op_size_calculator(cnn_layers[2]))

