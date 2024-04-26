use time::{PrimitiveDateTime, Duration};

pub fn after(start: PrimitiveDateTime) -> PrimitiveDateTime {
    const GIGA_SECOND: i64 = 1000000000;
    start.checked_add(Duration::seconds(GIGA_SECOND)).unwrap()

}
