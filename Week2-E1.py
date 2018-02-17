# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

spam = spam +3
print (text, spam)

{k: v for k, v in locals().items() if '_' not in k and 'pdb' not in k}