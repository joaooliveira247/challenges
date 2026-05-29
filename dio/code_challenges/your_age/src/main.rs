const CURRENT_DATE: (u8, u8, u16) = (29, 5, 2026);

fn main() {
    /* Given a year calcule the age of people */
    let name: &str = "John";
    let birth_year: u16 = 1998;
    let birth_month: u8 = 4;
    let birth_day: u8 = 16;

    let mut age: u16 = CURRENT_DATE.2 - birth_year;

    if CURRENT_DATE.1 < birth_month {
        age -= 1;
    } else if CURRENT_DATE.0 < birth_day && CURRENT_DATE.1 == birth_month {
        age -= 1;
    }

    println!("{} age is: {} years old", name, age)
}
