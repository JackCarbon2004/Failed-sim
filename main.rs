extern crate piston;
extern crate graphics;

use piston::window::WindowSettings;
use piston::event_loop::{Events, EventSettings};
use piston::input::RenderEvent;
use graphics::*;

fn main() {
    let mut window: PistonWindow =
        WindowSettings::new("Pendulum Animation", [640, 480])
            .exit_on_esc(true)
            .build()
            .unwrap();

    // Load pendulum data from file or data exchange format
    let pendulum_data = load_pendulum_data();

    while let Some(event) = window.next() {
        window.draw_2d(&event, |context, graphics, _device| {
            clear([1.0; 4], graphics);

            // Iterate over pendulum data and draw each pendulum
            for (i, pendulum) in pendulum_data.iter().enumerate() {
                let (x, y) = calculate_pendulum_position(pendulum);
                let color = get_pendulum_color(i);

                // Draw pendulum string
                line(color, 1.0, [0.0, 0.0, x, y], context.transform, graphics);

                // Draw pendulum bob
                ellipse(color, [x - 5.0, y - 5.0, 10.0, 10.0], context.transform, graphics);
            }
        });
    }
}