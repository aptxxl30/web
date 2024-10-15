def get_box_area(width, length, height):
    if width < 5 or length < 4 or height < 4:
        return 1
    box_area = width * length * height
    return box_area

box1=get_box_area(4,4,9)
box2=get_box_area(4,5,6)

print(box1)