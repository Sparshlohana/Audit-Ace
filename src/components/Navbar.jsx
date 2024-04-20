import Link from 'next/link'
import React from 'react'

const Navbar = () => {
    return (
        <nav className='shadow-md glass text-white'>
            <ul className='flex justify-center items-center gap-8 text-xl p-7'>
                <li><Link href={"/"}>Home</Link></li>
                <li><Link href={"/about"}>About</Link></li>
                <li><Link href={"/contact"}>Contact</Link></li>
                {/* <li><Link href={"/account"}>Accounts</Link></li> */}
                <li><Link href={"/help"}>Help</Link></li>
            </ul>
        </nav>
    )
}

export default Navbar