import math

def get_time(velocity, angle, x_position):
    return x_position / (velocity * math.cos(math.radians(angle)))

def get_y_position(velocity, time, angle):
    return velocity * time * math.sin(math.radians(angle)) - 0.5 * 9.81 * time * time

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        velocity, angle, x_position, h_min, h_max = map(float, input().split())
        time = get_time(velocity, angle, x_position)
        y_position = get_y_position(velocity, time, angle)
        if h_min + 1 < y_position and y_position < h_max - 1:
            print("Safe")
        else:
            print("Not Safe")

if __name__ == "__main__":
    main()
