import datetime


dt_replace = True
uranai_result = 100
dt_now = "20220000"
try:
    # dt_now = dt_now.strftime("%Y%m%d")
    dt_now = int(dt_now.replace('-', ''))
except Exception:
    dt_replace = False

print(dt_now)
print(len(str(dt_now)))

print(dt_replace)

print(datetime.date.today())

if not dt_replace:
    uranai_result = 1

if not len(str(dt_now)) == 8:
    print("not")

print(uranai_result)