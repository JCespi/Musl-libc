# python script that changes the values of the macros in 
# syscall.h.in

# "Macros"
UNUSED = "(-1)"
HLIMIT = 395
FILE = "syscall.h.in"

"""
@param lines a list of each line in syscall.h.in in string form
@param m_dict a dictionary with integer key that 
		      specifies line to change and integer value that 
			  specifies new value of macro on that line
"""
def initialize(lines, m_dict):
	output = []
	i = 0

	for line in lines:
		# do not modify lines after HLIMIT
		if i < HLIMIT:
			line = line.split()
			l_num = i + 1
			line[-1] = UNUSED if l_num not in m_dict else str(m_dict[l_num])
			line.append("\n")
			line = " ".join(line)
		i = i + 1
		
		# append line to output
		output.append(line)

	return output

def modify_syscall(lines_to_change = {}):
	# open and read syscall.h.in
	fr = open(FILE, mode = "r")
	lines = fr.readlines()
	fr.close()

	# modify the macros using a dictionary
	m_lines = initialize(lines, lines_to_change)

	# open and write syscall.h.in
	fw = open(FILE, mode = "w")
	fw.writelines(m_lines)
	fw.close()

def create_dict():
	# open and read sys_changes.txt
	fr = open("sys_changes.txt", mode = "r")
	lines = fr.readlines()
	fr.close()
	
	output_dict = {}
	for line in lines:
		line = line.split(",")

		if len(line) == 2:
			output_dict[int(line[0])] = int(line[1])

	return output_dict	

def main():
	# no need to worry about indexing. just enter lines as seen in file
	lines_to_change = create_dict()
	modify_syscall(lines_to_change) 

if __name__ == "__main__":
	main()
	
