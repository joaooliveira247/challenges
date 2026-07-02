use axum::Router;
use sqlx::PgPool;
use tokio::net::TcpListener;
use tracing::info;
use tracing_subscriber::{
    Layer, fmt::format::FmtSpan, layer::SubscriberExt, util::SubscriberInitExt,
};

use crate::routes::api::router;

#[derive(Clone)]
pub struct AppState {
    pub db: PgPool,
}

impl AppState {
    pub async fn new() -> color_eyre::Result<Self> {
        let db_url = std::env::var("DATABASE_URL")?;
        let db = PgPool::connect(&db_url).await?;
        Ok(Self { db })
    }
}

pub struct App;

impl App {
    pub async fn start() -> color_eyre::Result<()> {
        let layer = tracing_subscriber::fmt::layer()
            .with_span_events(FmtSpan::NEW)
            .boxed();

        tracing_subscriber::registry().with(layer).init();

        dotenvy::dotenv()?;
        let state = AppState::new().await?;

        let listener = TcpListener::bind("127.0.0.1:8000").await?;
        let router = Router::new().nest("/api", router()).with_state(state);
        axum::serve(listener, router).await?;

        info!("🚀 Starting service at: 127.0.0.1:8000");

        Ok(())
    }
}