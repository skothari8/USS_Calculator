
from tkinter import *
import math

def calculate_scales():
    # Get L-NIHSS scores from the user inputs
    l_nihss = {
        '1A': int(e1A.get()),
        '1B': int(e1B.get()),
        '1C': int(e1C.get()),
        '1D': int(e1D.get()),
        '2': int(e2.get()),
        '3': int(e3.get()),
        '4': int(e4.get()),
        '5A': int(e5A.get()),
        '5B': int(e5B.get()),
        '6A': int(e6A.get()),
        '6B': int(e6B.get()),
        '7': int(e7.get()),
        '8': int(e8.get()),
        '9': int(e9.get()),
        '10': int(e10.get()),
        '11': int(e11.get())
    }
    # NIHSS
    total_sum = sum(l_nihss.values())
    lbl_nihss_score.config(text=f"NIHSS: {total_sum}")
    
    # BE-FAST
    be_fast = sum([l_nihss[key] > 0 for key in ['7', '3', '4', '5A', '5B', '6A', '6B', '9', '10']])
    lbl_be_fast.config(text=f"BE-FAST: {'Positive' if be_fast > 0 else 'Negative'}")

    # VAN Scale
    temp1 = sum([l_nihss[key] > 0 for key in ['5A', '5B', '6A', '6B']])
    temp2 = sum([l_nihss[key] > 0 for key in ['3', '9', '2', '11']])
    van = 0
    if ((temp1 > 0) & (temp2 > 0)):
        van = temp1 + temp2
    lbl_van.config(text=f"VAN: {'Positive' if ((temp1 > 0) & (temp2 > 0)) else 'Negative'}")

    # LAMS
    lams = 0
    if l_nihss['4'] > 0:
        lams += 1
    if (1 <= l_nihss['5A'] <= 2) or (1 <= l_nihss['5B'] <= 2):
        lams += 1
    if (l_nihss['5A'] == 3) or (l_nihss['5B'] == 3):
        lams += 2
    if (l_nihss['5A'] == 4) or (l_nihss['5B'] == 4):
        lams += 1
    if l_nihss['1D'] == 1:
        lams += 1
    if l_nihss['1D'] == 2:
        lams += 2
    if lams > 5:
        lams = 5

    lbl_lams.config(text=f"LAMS: {lams} - {'High LVO' if lams >= 4 else 'Low LVO'}")

    # FAST-ED
    fast_ed = 0
    if l_nihss['4'] > 0:
        fast_ed += 1
    motor_score = 0
    if (1 <= l_nihss['5A'] <= 2) or (1 <= l_nihss['5B'] <= 2):
        motor_score = 1
    if (l_nihss['5A'] >= 3) or (l_nihss['5B'] >= 3):
        motor_score = 2
    fast_ed += motor_score
    if (l_nihss['9'] > 0) or (l_nihss['10'] > 0):
        fast_ed += 1
    if (l_nihss['9'] > 1) or (l_nihss['10'] > 1):
        fast_ed += 1
    if fast_ed > 9:
        fast_ed = 9
    fast_ed = fast_ed + l_nihss['2'] + l_nihss['11']
    lbl_fast_ed.config(text=f"FAST-ED: {fast_ed} - {'High LVO' if fast_ed >= 4 else 'Low LVO'}")

    race = 0
    facial_palsy_score = 0
    if l_nihss['4'] > 0:
        facial_palsy_score = 1  
    if l_nihss['4'] > 1:
        facial_palsy_score = 2  
    race += facial_palsy_score  
    arm_weakness_score = 0
    if (1 <= l_nihss['5A'] <= 2) or (1 <= l_nihss['5B'] <= 2):
        arm_weakness_score = 1  
    if (l_nihss['5A'] >= 3) or (l_nihss['5B'] >= 3):
        arm_weakness_score = 2  
    race += arm_weakness_score  
    leg_weakness_score = 0
    if (1 <= l_nihss['6A'] <= 2) or (1 <= l_nihss['6B'] <= 2):
        leg_weakness_score = 1 
    if (l_nihss['6A'] >= 3) or (l_nihss['6B'] >= 3):
        leg_weakness_score = 2 
    race += leg_weakness_score  
    if l_nihss['2'] > 0:
        race += 1
    if l_nihss['9'] == 1:
        race += 1  
    if l_nihss['9'] >= 2:
        race += 2  
    if l_nihss['11'] == 1:
        race += 1 
    if l_nihss['11'] == 2:
        race += 2 
    if race > 11:
        race = 11  
    lbl_race.config(text=f"RACE: {race} - {'High LVO' if race >= 5 else 'Low LVO'}")


    # 3-ISS
    iss_3 = 0
    if l_nihss['1A'] > 0:
        iss_3 += 1
    if l_nihss['1A'] > 1:
        iss_3 += 1
    if l_nihss['2'] == 1:
        iss_3 += 1
    if l_nihss['2'] == 2:
        iss_3 += 2
    if (1 <= l_nihss['5A'] <= 2) or (1 <= l_nihss['5B'] <= 2) or (1 <= l_nihss['6A'] <= 2) or (1 <= l_nihss['6B'] <= 2):
        motor_score = 1
    if (l_nihss['5A'] >= 3) or (l_nihss['5B'] >= 3) or (l_nihss['6A'] >= 3) or (l_nihss['6B'] >= 3):
        motor_score = 2
    iss_3 += motor_score
    if iss_3 > 6:
        iss_3 = 6
    lbl_iss_3.config(text=f"3-ISS: {iss_3} - {'High LVO' if iss_3 >= 4 else 'Low LVO'}")

    # PASS
    pass_scale = 0
    if l_nihss['1B'] > 0:
        pass_scale += 1
    if l_nihss['2'] > 0:
        pass_scale += 1
    if max(l_nihss['5A'], l_nihss['5B']) > 0:
        pass_scale += 1
    if pass_scale > 3:
        pass_scale = 3
    lbl_pass.config(text=f"PASS: {pass_scale} - {'High LVO' if pass_scale >= 2 else 'Low LVO'}")

    # LARIO
    lario = 0
    if l_nihss['4'] > 0:
        lario += 1
    if (0 < l_nihss['5A']) or (0 < l_nihss['5B']):
        lario += 1
    if (l_nihss['9'] > 0) or (l_nihss['10'] > 0):
        lario += 1
    if l_nihss['11'] == 1:
        lario += 1
    if l_nihss['11'] == 2:
        lario += 2
    if lario > 5:
        lario = 5
    lbl_lario.config(text=f"LARIO: {lario} - {'High LVO' if lario > 3 else 'Low LVO'}")

    # List of scales with their sensitivities and specificities
    scales = [
        {"name": "BE-FAST", "sens": 0.68, "spec": 0.85, "value": be_fast > 0},
        {"name": "VAN", "sens": 1.0, "spec": 0.9, "value": van > 1},
        {"name": "LAMS", "sens": 0.81, "spec": 0.89, "value": lams >= 4},
        {"name": "FAST-ED", "sens": 0.6, "spec": 0.89, "value": fast_ed >= 4},
        {"name": "RACE", "sens": 0.85, "spec": 0.68, "value": race >= 5},
        {"name": "3-ISS", "sens": 0.67, "spec": 0.92, "value": iss_3 >= 4},
        {"name": "PASS", "sens": 0.66, "spec": 0.83, "value": pass_scale >= 2},
        {"name": "LARIO", "sens": 1.0, "spec": 0.82, "value": lario > 3},
    ]

    # Filter scales that meet the High LVO criteria
    high_lvo_scales = [scale for scale in scales if scale['value']]
    
    sensitivity = [scale['sens'] for scale in scales if scale['value']]
    specificity = [scale['spec'] for scale in scales if scale['value']]
    
    # Calculate parallel sensitivity and specificity for scales that meet the High LVO criteria
    parallel_sens = 0
    if len(high_lvo_scales) > 0 :
        parallel_sens = 1 - math.prod(sensitivity)
    
    parallel_spec = -1
    if len(high_lvo_scales) > 0 :
        if len(high_lvo_scales) == 1:
            parallel_spec = sum(sensitivity) - math.prod(sensitivity)
        else:
            parallel_spec = math.prod(specificity)
    
    lbl_parallel_sens.config(
        text=f"Parallel Sensitivity: {parallel_sens * 100:.2f}%" if parallel_sens > 0 else "Parallel Sensitivity: N/A")
    lbl_parallel_spec.config(
        text=f"Parallel Specificity: {parallel_spec * 100:.2f}%" if parallel_spec >= 0 else "Parallel Specificity: N/A")

# Initialize Tkinter
root = Tk()
root.title("Ultimate Stroke Scale")

# Create L-NIHSS input fields and labels
e1A = Entry(root)
e1A.grid(row=0, column=1)
Label(root, text="1A: Level of Consciousness").grid(row=0)

e1B = Entry(root)
e1B.grid(row=1, column=1)
Label(root, text="1B: Ask month and age").grid(row=1)

e1C = Entry(root)
e1C.grid(row=2, column=1)
Label(root, text="1C: Command patient to Blink eyes").grid(row=2)

e1D = Entry(root)
e1D.grid(row=3, column=1)
Label(root, text="1D: Command patient to Squeeze Hands").grid(row=3)

e2 = Entry(root)
e2.grid(row=4, column=1)
Label(root, text="2: Horizontal extraocular movements").grid(row=4)

e3 = Entry(root)
e3.grid(row=5, column=1)
Label(root, text="3: Visual Fields").grid(row=5)

e4 = Entry(root)
e4.grid(row=6, column=1)
Label(root, text="4: Facial Palsy").grid(row=6)

e5A = Entry(root)
e5A.grid(row=7, column=1)
Label(root, text="5A: Left Arm Motor Drift").grid(row=7)

e5B = Entry(root)
e5B.grid(row=8, column=1)
Label(root, text="5B: Right Arm Motor Drift").grid(row=8)

e6A = Entry(root)
e6A.grid(row=9, column=1)
Label(root, text="6A: Left Leg Motor Drift").grid(row=9)

e6B = Entry(root)
e6B.grid(row=10, column=1)
Label(root, text="6B: Right Leg Motor Drift").grid(row=10)

e7 = Entry(root)
e7.grid(row=11, column=1)
Label(root, text="7: Limb Ataxia").grid(row=11)

e8 = Entry(root)
e8.grid(row=12, column=1)
Label(root, text="8: Sensation").grid(row=12)

e9 = Entry(root)
e9.grid(row=13, column=1)
Label(root, text="9: Language/Aphasia").grid(row=13)

e10 = Entry(root)
e10.grid(row=14, column=1)
Label(root, text="10: Dysarthria").grid(row=14)

e11 = Entry(root)
e11.grid(row=15, column=1)
Label(root, text="11: Extinction/inattention").grid(row=15)

# Create buttons and result labels
Button(root, text="Calculate", command=calculate_scales).grid(row=16, columnspan=2)

lbl_nihss_score = Label(root, text="NIHSS:")
lbl_nihss_score.grid(row=27, column=0)

lbl_be_fast = Label(root, text="BE-FAST:")
lbl_be_fast.grid(row=17, column=0)

lbl_van = Label(root, text="VAN:")
lbl_van.grid(row=18, column=0)

lbl_lams = Label(root, text="LAMS:")
lbl_lams.grid(row=19, column=0)

lbl_fast_ed = Label(root, text="FAST-ED:")
lbl_fast_ed.grid(row=20, column=0)

lbl_race = Label(root, text="RACE:")
lbl_race.grid(row=21, column=0)

lbl_iss_3 = Label(root, text="3-ISS:")
lbl_iss_3.grid(row=22, column=0)

lbl_pass = Label(root, text="PASS:")
lbl_pass.grid(row=23, column=0)

lbl_lario = Label(root, text="LARIO:")
lbl_lario.grid(row=24, column=0)

lbl_parallel_sens = Label(root, text="Parallel Sensitivity:")
lbl_parallel_sens.grid(row=25, column=0)

lbl_parallel_spec = Label(root, text="Parallel Specificity:")
lbl_parallel_spec.grid(row=26, column=0)

root.mainloop()
