# MacVendor identifier.
# The mac address consist in 12 alphanumeric digits, the firts 6 are the vendor identifier.

print("#######################################################################")
print("#######################################################################")
print("#######################################################################")
print("########################## MACVENDOR identifier #######################")
print("#######################################################################")
print("#######################################################################")
print("#######################################################################")
def main():
	 

	vendorlist = {};

	with open("mac.txt",encoding="utf-8") as datos:
		for line in datos:
			vendorlist[line[0:6]] = line[7:57];

	mac = input("MAC -> ")

	mac.upper()

	if mac[2] == "-" or mac[2] == ":":

		mac = mac.replace("-","")
		mac = mac.replace(":","")

	if len(mac) > 6:
		mac = mac[:6]

	print("\n",vendorlist.get(mac))


while True:
	main()