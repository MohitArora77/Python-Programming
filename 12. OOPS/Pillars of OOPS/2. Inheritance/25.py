class Bat:
    b_length="38 inch"
    b_weight="1.5 kg"
    b_quality="Good"
class Ball:
    ba_weight="200 g"
    ba_color="Red"
    ba_tenacity="Hard"
class Pitch:
    p_long="20.12 m"
    p_wide="3.05 m"
    p_shape="Rectangular"
class Cricket(Bat,Ball,Pitch):
    no_player="11 Players"
    
print("Bat -->",Cricket.b_length,Cricket.b_quality,Cricket.b_weight)
print("Ball -->",Cricket.ba_color,Cricket.ba_tenacity,Cricket.ba_weight)
print("Pitch -->",Cricket.p_long,Cricket.p_wide,Cricket.p_shape)
print("No_of_Players -->",Cricket.no_player)
    