import { Inter } from "next/font/google";
import "./globals.css";
const inter = Inter({ subsets: ["latin"] });
import 'react-toastify/dist/ReactToastify.css';

export const metadata = {
  title: "Audit Ace",
  description: "Using AI to leverage accountants",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        {children}
      </body>
    </html>
  );
}
