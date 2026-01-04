export interface User {
    id: number;
    username: string;
    email: string;
}

export interface LoginData {
    username: string;
    password: string;
}

export interface RegisterData {
    username: string;
    email: string;
    password: string;
}

export interface BackendResponse {
    responses: string[];
}

export interface AuthResponse {
    access_token: string;
    token_type: string;
    user: User;
}