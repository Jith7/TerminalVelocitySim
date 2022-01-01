import argparse
import matplotlib.pyplot as plt


def simulate(args):

    initial_h = args.height
    drag_co = args.drag_co
    g = args.g
    m = args.mass
    h = initial_h
    t = 0
    step = args.time
    v = 0
    deployed = False
    out = []
    while h >= 0:
        drag_f1 = (drag_co * v**2) / 2
        a = (m*g - drag_f1) / m
        u = v
        h -= (u*step + 0.5*a*step**2)
        if h < args.para and not deployed:
            deployed = True
            drag_co = drag_co + 10.0
        v = v + a*step
        if v <= 0:
            v = 0
        #print(f"at time {t} - height {h}m, suvats : {u,v,a}")
        out.append((t, u, v, a, h))
        t += step

    return out


def main():

    parser = argparse.ArgumentParser(
        description=" Terminal Velocity Simulator ")
    parser.add_argument("--height", type=float, required=True)
    parser.add_argument("--mass", type=float, required=True)
    parser.add_argument("--drag_co", type=float, required=True)
    parser.add_argument("--g", type=float, default=9.81, required=False)
    parser.add_argument("--time", type=float, default=1, required=False)
    parser.add_argument("--para", type=float, default=-1, required=False)
    parser.add_argument("--out", type=str, default="", required=False)
    args = parser.parse_args()
    # print(args)

    data = simulate(args)
    x = [item[0] for item in data]
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(x, [item[1] for item in data])
    axs[0, 0].set_title("initial velocity")

    axs[0, 1].plot(x, [item[2] for item in data])
    axs[0, 1].set_title("Final velocity")

    axs[1, 0].plot(x, [item[3] for item in data])
    axs[1, 0].set_title("acceleration")

    axs[1, 1].plot(x, [item[4] for item in data])
    axs[1, 1].set_title("height")

    plt.suptitle(f"Terminal Velocity Sim : {args.height}m, {args.mass}kg, drag coefficient {args.drag_co}")

    if args.out:
        fig.set_size_inches(19.2, 10.8)

        plt.savefig(args.out, bbox_inches='tight', dpi=100)
    else:
        plt.show()


if __name__ == "__main__":
    main()
