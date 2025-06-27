h = float(input('altura da sala em metros: '))
c = float(input('comprimento da sala em metros: '))
l = float(input('largura da sala em metros: '))

area = l * c
volume = l * c * h
area_das_paredes = (2 * h * l) + (2 * h * c)

print(f'a área do piso da sala tem {area} metros quadrados \no volume da sala é de {volume} metros cúbicos \na área das paredes da sala é de {area_das_paredes} metros quadrados')