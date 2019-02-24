import sys, os, subprocess

def getErrors(sourcefile):
# ~/code/bin/lean-3.4.2-linux/bin/lean --run
	ret = []
	pr = subprocess.Popen(['/home/chinmaya/code/bin/lean-3.4.2-linux/bin/lean', '--run', sourcefile],  stdout=subprocess.PIPE, stdin=subprocess.PIPE,stderr=subprocess.PIPE)

	output, err = pr.communicate()

	p = output.decode('utf-8').split("\n")

	if len(p) == 2:
		ret.append("No errors!")
	else:
		ret.append("Errors were found. Failure at point: ")
		ret.append(p[len(p)-3])
	return ret

sourcefile = "actual_transpile.lean"
errors = getErrors(sourcefile)
for i in errors:
	print(i)
