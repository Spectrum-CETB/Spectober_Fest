import React from "react";
import { Typography, Space } from "antd";
import { FaInstagram, FaLinkedin, FaTwitter } from "react-icons/fa";

const Footer = () => {
  const footerYear = new Date().getFullYear();
  return (
    <footer className="footer">
      <Typography.Title
        level={5}
        style={{ color: "white", textAlign: "center" }}
      >
        &copy;{footerYear} Prateek Rath . CryptoVerse
      </Typography.Title>
      <Space>
        <a href="https://www.linkedin.com/in/prateek-rath-9a9779219/">
          <FaLinkedin />
        </a>
        <a href="https://twitter.com/iampsr8">
          <FaTwitter />
        </a>
        <a href="https://www.instagram.com/i_am_psr8/">
          <FaInstagram />
        </a>
      </Space>
    </footer>
  );
};

export default Footer;
