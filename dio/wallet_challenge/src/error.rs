use axum::{
    Json,
    http::{StatusCode, status},
    response::{IntoResponse, Response},
};
use serde::Serialize;
use thiserror::Error;

#[derive(Error, Debug)]
pub enum AppError {
    #[error("Missing Authorization Header")]
    MissingAuthorization,
    #[error("Invalid Credential")]
    InvalidCredentials,
    #[error("Asset does not exist")]
    AssetDoesNotExist,
    #[error(transparent)]
    Database(#[from] sqlx::Error),
}

#[derive(Serialize)]
pub struct ErrorResponse {
    error: String,
}

impl IntoResponse for AppError {
    fn into_response(self) -> Response {
        let error_response = ErrorResponse {
            error: self.to_string(),
        };

        let status = match self {
            Self::MissingAuthorization => StatusCode::BAD_REQUEST,
            Self::InvalidCredentials => StatusCode::UNAUTHORIZED,
            Self::AssetDoesNotExist => StatusCode::NOT_FOUND,
            Self::Database(..) => StatusCode::INTERNAL_SERVER_ERROR,
        };

        (status, Json(error_response)).into_response()
    }
}
