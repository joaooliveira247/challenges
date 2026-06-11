use std::{process::Command, thread::sleep, time::Duration};

pub fn clear() {
    if cfg!(target_os = "windows") {
        Command::new("cmd")
            .args(["/C", "cls"])
            .status()
            .expect("Failed to clean terminal.");
    } else {
        Command::new("clear")
            .status()
            .expect("Failed to clean terminal.");
    }
}

pub fn wait(time: u64) {
    sleep(Duration::from_secs(time))
}
