fn diff_squares(n: i32) -> i32 {
    let mut square_sum_a = Vec::new();
    let mut sum_square_b = Vec::new();

    for i in 1..n + 1 {
        square_sum_a.push(i);
        sum_square_b.push(i.pow(2));
    }
    let sum_a: i32 = square_sum_a.iter().sum();
    println!("{}", sum_a.pow(2));
    let sum_b: i32 = sum_square_b.iter().sum();
    println!("{}", sum_b);
    sum_a.pow(2) - sum_b
}

fn main() {
    let answ = diff_squares(10);
    println!("Answer: {}", answ);
}
