fn reverse(word: String) -> String {
    let reversed: String = word.chars().rev().collect();
    reversed
}

fn main() {
    let word = String::from("Brave");
    println!("{}", reverse(word));
}
