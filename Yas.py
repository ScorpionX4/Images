from turtledemo.chaos import f

price=(100)
is_Vedant_coming=True
is_taksh_coming=False

if is_Vedant_coming and is_taksh_coming:
    Total= price/ 3
    print(f"Equal =  ₹{Total} " 'between 3')
elif is_taksh_coming or is_Vedant_coming:

    Total= price/2                                # I want to put the True value in the ? place.
    print(f"Equal = ₹{Total} . "'Equal between me and ? ')
if not is_Vedant_coming and not is_taksh_coming:
    Total= '₹'+str(price)
    print(Total+' All mine')
