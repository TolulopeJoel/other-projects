import React, { useState, useEffect } from "react";
import api from "../components/api";
import Navbar from "../components/Navbar";

export default function Profile() {
    const [userDetails, setUserDetails] = useState({ results: [] });

    useEffect(() => {
        api.get('/profile/')
            .then((response) => {
                console.log(response.data);
                setUserDetails(response.data);
            })
            .catch((error) => {
                console.error(error);
            })
    }, []);

    return (
        <>
            <Navbar />
            {userDetails && (
                <>
                    <h1>PROfile</h1>
                    {userDetails.results && userDetails.results.map(user => (
                        <div class="row u-add-half-bottom">
                            <div class="column lg-6 tab-12">
                                <figure class="profile-photo">
                                    <img src={user.profile_picture} alt="profile-photo" class="avatar" />
                                </figure>

                                <h2><b>@{user.username}</b></h2>
                                <span><b>{user.first_name} {user.last_name}</b></span>
                                <p>{user.bio}</p>
                            </div>
                            <div class="column lg-6 tab-12">
                                <p><a class='btn btn--stroke u-fullwidth' href="">edit your profile</a>
                                    <a class='btn btn--stroke u-fullwidth' href="">Create Post</a>
                                    <a class='btn btn--stroke u-fullwidth' href="">Manage Posts</a>
                                    <a class='btn btn--stroke u-fullwidth' href="">Delete account</a>
                                    <a class='btn btn--stroke u-fullwidth' href="">Invite a friend</a></p>
                            </div>
                        </div>
                    ))}
                </>
            )}
            {!userDetails && (
                <p>Loading...</p>
            )}
        </>
    )
}
