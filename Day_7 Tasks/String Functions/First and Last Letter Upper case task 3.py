text ="candy_preethi"
if len(text)>=2:
    result = text[0].upper()+text[1:-1]+text[-1].upper()
elif len(text)==1:
    result = text.upper()
else:
     result=" "
print(result)
