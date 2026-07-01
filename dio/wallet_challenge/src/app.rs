use std::{collections::HashMap, sync::Arc};

use axum::Router;
use tokio::{net::TcpListener, sync::Mutex};
use tracing::info;
use tracing_subscriber::{
    Layer, fmt::format::FmtSpan, layer::SubscriberExt, util::SubscriberInitExt,
};

use crate::{models::assets::Asset, routes::api::router};

#[derive(Clone)]
pub struct AppState {
    pub assets: Arc<Mutex<HashMap<i64, Asset>>>,
}

impl AppState {
    pub fn new() -> Self {
        Self {
            assets: Default::default(),
        }
    }
}

pub struct App;

impl App {
    pub async fn start() -> color_eyre::Result<()> {
        let layer = tracing_subscriber::fmt::layer()
            .with_span_events(FmtSpan::NEW)
            .boxed();

        tracing_subscriber::registry().with(layer).init();

        let listener = TcpListener::bind("127.0.0.1:8000").await?;
        let router = Router::new()
            .nest("/api", router())
            .with_state(AppState::new());
        axum::serve(listener, router).await?;

        info!("🚀 Starting service at: 127.0.0.1:8000");

        Ok(())
    }
}
