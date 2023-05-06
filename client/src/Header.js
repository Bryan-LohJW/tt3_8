const Header = (props) => {
  return (
    <header>
        <h1 style={{color: 'red', backgroundColor: 'black'}} >Task Tracker</h1>
        <h1>{props.title}</h1>
    </header>
  )
}

Header.defaultProps = {
    title: 'Task',
}

Header.propTypes = {
    title: propTypes.string.isRequired,
}

export default Header
