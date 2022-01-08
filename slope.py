import numpy as np
import argparse


def slope_grad(drop, length):
	tan_theta = drop / length

	theta = np.degrees(np.arctan(tan_theta))
	slope = tan_theta * 100

	return slope, theta


def ls(length, slope):
	"""
	(L/22)^{0.5} (0.065 + 0.045S + 0.0065S^2)
	"""
	ls_val = (length / 22) ** 0.5 * (0.065 + 0.045 * slope + 0.0065 * slope * slope)
	return ls_val


def convert(length):
	return length * 20


def arg_parse():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--drop", type=float, default=False,
						help="drop", dest="drop")
	parser.add_argument("-l", "--length", type=float, default=False,
						help="length", dest="length")
	parser.add_argument("-c", type=bool, default=False,
						help="convert", dest="conv")

	return parser.parse_args()


def main():
	args = arg_parse()

	drop = convert(args.drop) if args.conv else args.drop

	slope, theta = slope_grad(drop, args.length)
	ls_val = ls(args.length, slope)

	print(f"Slope in %:\t{slope}")
	print(f"       deg:\t{theta}")
	print(f"LS:\t\t{ls_val}")


if __name__ == '__main__':
	main()
