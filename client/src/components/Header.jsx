import { Outlet, Link } from 'react-router-dom';
import classes from './Header.module.css';

const Header = () => {
	return (
		<>
			<div className={classes.body}>
				<div className={classes.header}>
					<div className={classes.logo}></div>
					<div className={classes.links}>
						<Link to={'/dashboard'} className={classes.action}>
							<p>Home</p>
						</Link>
						<Link to={'/createClaim'} className={classes.action}>
							<p>Create Claim</p>
						</Link>
						<Link to={'/'} className={classes.action}>
							<p>Logout</p>
						</Link>
					</div>
				</div>
			</div>
			<div className={classes.outlet}>
				<Outlet />
			</div>
		</>
	);
};

export default Header;
