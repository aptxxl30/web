def celsius_to_fahrenheit(celsius):
  """แปลงอุณหภูมิจากองศาเซลเซียสเป็นองศาฟาเรนไฮต์

  Args:
    celsius: อุณหภูมิในหน่วยองศาเซลเซียส

  Returns:
    อุณหภูมิในหน่วยองศาฟาเรนไฮต์
  """

  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

# รับค่าอุณหภูมิในหน่วยองศาเซลเซียสจากผู้ใช้
celsius = float(input("กรุณากรอกอุณหภูมิในหน่วยองศาเซลเซียส: "))

# เรียกใช้ฟังก์ชันเพื่อแปลงหน่วย
fahrenheit = celsius_to_fahrenheit(celsius)

# แสดงผลลัพธ์
print(f"{celsius} องศาเซลเซียส เท่ากับ {fahrenheit} องศาฟาเรนไฮต์")
