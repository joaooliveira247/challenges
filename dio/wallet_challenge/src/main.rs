use wallet_challenge::app::App;

#[tokio::main]
async fn main() -> color_eyre::Result<()> {
    App::start().await
}
