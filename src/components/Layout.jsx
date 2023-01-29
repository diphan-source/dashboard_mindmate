import React from "react";
import Navbar from "./Navbar";

const Layout = ({ children }) => {
  return (
    <div className="page-wrapper compact-wrapper" id="pageWrapper">
      <div className="page-header">
        <Navbar />
      </div>
      <div className="page-body-wrapper">
        <div className="sidebar-wrapper">{/* sidebar here */}</div>
        <div className="page-body">{children}</div>
        <footer className="footer">
          <div className="container-fluid">
            <div className="row">
              <div className="col-md-12 footer-copyright text-center">
                <p className="mb-0">
                  Copyright {new Date().getFullYear()} © Mindmate{" "}
                </p>
              </div>
            </div>
          </div>
        </footer>
      </div>
    </div>
  );
};

export default Layout;
