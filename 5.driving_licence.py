from datetime import datetime

def driver(data):
    first, middle, surname, dob, gender = data

    #Գրվում է մեծատառերով Եթե պակաս է 5 սիմվոլից,լրացվում է 9-երով օր. "Lee" → "LEE99"
    surname_code = (surname.upper() + '99999')[:5]

    # Ստանում ենք datetime օբյեկտ՝ անկախ նրանից, թե ամիսը կրճատ (Jan) է, թե ամբողջական (January)։
    try:
        dt = datetime.strptime(dob, "%d-%B-%Y")
    except ValueError:
        dt = datetime.strptime(dob, "%d-%b-%Y")

    year = dt.year
    month = dt.month
    day = dt.day

    #Այս կոդը վերցնում է ծննդյան տարվա երրորդ թվանշանը։ (1987 → '8')
    decade_digit = str(year)[2]

    #Ամսվա համարը սեռով տղու դեպքում 01-12,կնոջ 51-62
    if gender.upper() == 'F':
        month += 50
    month_code = f"{month:02d}"

    #ամսվա օրերը միշտ 2նիշ օրինակ՝ 01, 14, 31
    day_code = f"{day:02d}"

    #տարվա վերջին Թիվը օր, 1987 -> "7", 2000 -> 0
    year_digit = str(year)[3]

 #  վերձնում ենք անունի ու հայրանունի սկզբի տառերը,եթե հայրանում չկա դնում ենք "9"
    initials = first[0].upper()
    initials += middle[0].upper() if middle else '9'

    #  always 9
    #  always AA
    return surname_code + decade_digit + month_code + day_code + year_digit + initials + "9AA"

#driver(["Sargis","Harutyun","Matevosyan","06-Feb-2001","M"])
print(driver)

