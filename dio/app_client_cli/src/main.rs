use app_client_cli::Customer;

fn main() {
    let customer_1 = Customer::new(
        1,
        String::from("John"),
        String::from("123.456.789-0"),
        String::from("Rua dos bobos, n° 8"),
    );

    println!("{:?}", customer_1);
}
