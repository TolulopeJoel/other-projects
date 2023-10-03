import React from "react";
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import PostDetail from "./pages/PostDetail";
import Profile from './pages/Profile';
import PostList from './pages/PostList';
import SignIn from "./components/Auth/SignIn";
import SignUp from "./components/Auth/SignUp";

export default function PagePaths() {
    return (
        <BrowserRouter>
            <Routes>
                <Route index element={<PostList />} />
                <Route path="/blog/:postSlug/" element={<PostDetail />} />
                <Route path="/sign-in" element={<SignIn />} />
                <Route path="/sign-up" element={<SignUp />} />
                <Route path="/profile" element={<Profile />} />
            </Routes>
        </BrowserRouter>
    )
}