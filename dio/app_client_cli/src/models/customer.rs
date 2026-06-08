#[derive(Debug)]
pub struct Customer {
    id: i32,
    name: String,
    ssn: String,
    address: String,
}

impl Customer {
    pub fn new(id: i32, name: String, ssn: String, address: String) -> Customer {
        Customer {
            id,
            name,
            ssn,
            address,
        }
    }
}
