import json
import math

def simulate_pendulum(length, time_steps, dt):
    g = 9.81  # Acceleration due to gravity
    theta_0 = 1.0  # Initial angular displacement
    omega_0 = 0.0  # Initial angular velocity

    theta = [theta_0]
    omega = [omega_0]
    time = [0.0]

    for i in range(1, time_steps):
        t = i * dt
        theta_prev = theta[i - 1]
        omega_prev = omega[i - 1]

        # Calculate angular acceleration
        alpha = -g / length * math.sin(theta_prev)

        # Update angular velocity and displacement using the Euler method
        omega_new = omega_prev + alpha * dt
        theta_new = theta_prev + omega_new * dt

        theta.append(theta_new)
        omega.append(omega_new)
        time.append(t)

    return theta, omega, time

def export_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def main():
    lengths = [4, 8, 10, 15]  # Pendulum lengths
    time_steps = 1000  # Number of time steps
    dt = 0.01  # Time step size

    pendulum_data = {}

    for length in lengths:
        theta, omega, time = simulate_pendulum(length, time_steps, dt)
        pendulum_data[str(length)] = {
            'theta': theta,
            'omega': omega,
            'time': time
        }

    export_to_json(pendulum_data, 'pendulum_data.json')
    print("Pendulum data exported to pendulum_data.json")

if __name__ == '__main__':
    main()