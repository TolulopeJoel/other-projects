import React from "react";
import { useNavigate } from "react-router-dom";

export default function Navbar() {
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            localStorage.removeItem("access_token");
            navigate("/sign-in");
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <>
            <header id="masthead" className="s-header">

                <div className="s-header__branding">
                    <p className="site-title">
                        <a href="index.html" rel="home">Terava.</a>
                    </p>
                </div>

                <div className="row s-header__navigation">

                    <nav className="s-header__nav-wrap">

                        <h3 className="s-header__nav-heading">Navigate to</h3>

                        <ul className="s-header__nav">
                            <li><a href="">Go back</a></li>
                            <li className="current-menu-item">
                                <a href="/">Home</a>
                            </li>
                            <li><a href="">Trending</a></li>
                            <li><a href="/profile">Profile</a></li>
                            <li>
                                <form onSubmit={handleSubmit}>
                                    <input type="submit" value="Logout"></input>
                                </form>
                            </li>
                        </ul>

                    </nav>

                </div>

                <a className="s-header__menu-toggle" href="#0"><span>Menu</span></a>

            </header>
        </>
    );
}
