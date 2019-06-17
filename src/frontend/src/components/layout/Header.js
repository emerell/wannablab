import React, { Component } from 'react';
import { Link } from 'react-router-dom';

export class Header extends Component {
    render() {
        return (
            <nav className="navbar navbar-expand-sm navbar-light">
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse navbar" id="navbarTogglerDemo01">
                    <a className="navbar-brand" href="#">
                        <div className="logo">WB</div>
                    </a>
                    <ul className="navbar-nav ml-auto mt-2 mt-lg-0">
                        <li className="nav-item">
                            <Link
                                to="/register"
                                className="nav-link header__link">Register</Link>
                        </li>
                        <li className="nav-item">
                            <Link
                                to="/login"
                                className="nav-link header__link">Log in</Link>
                        </li>
                    </ul>
                </div>
            </nav>
        )
    }
}

export default Header;