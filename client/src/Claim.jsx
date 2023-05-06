< !DOCTYPE html >
    <html>
        <head>
            <title>Claim Management System</title>
            <script src="https://unpkg.com/react@16.14.0/umd/react.production.min.js"></script>
            <script src="https://unpkg.com/react-dom@16.14.0/umd/react-dom.production.min.js"></script>
            <script src="https://unpkg.com/babel-standalone@6.26.0/babel.min.js"></script>
        </head>
        <body>
            <div id="root"></div>11

            <script type="text/babel">
    // Claim form component
                class ClaimForm extends React.Component {
                    constructor(props) {
                    super(props);
                this.state = {
                    firstName: '',
                lastName: '',
                date: '',
                amount: '',
                purpose: '',
                image: null,
                followUp: false,
                previousClaimId: ''
        };
      }

      handleChange = (event) => {
        const {name, value} = event.target;
                this.setState({[name]: value });
      }

      handleImageChange = (event) => {
                    this.setState({ image: event.target.files[0] });
      }

      handleSubmit = (event) => {
                    event.preventDefault();
                // Perform form submission logic here
                console.log('Form submitted!', this.state);
                // Reset form fields
                this.setState({
                    firstName: '',
                lastName: '',
                date: '',
                amount: '',
                purpose: '',
                image: null,
                followUp: false,
                previousClaimId: ''
        });
      }

                render() {
        const {
                    firstName,
                    lastName,
                    date,
                    amount,
                    purpose,
                    followUp,
                    previousClaimId
                } = this.state;

                return (
                <form onSubmit={this.handleSubmit}>
                    <label>
                        First Name:
                        <input
                            type="text"
                            name="firstName"
                            value={firstName}
                            onChange={this.handleChange}
                        />
                    </label>
                    <br />
                    <label>
                        Last Name:
                        <input
                            type="text"
                            name="lastName"
                            value={lastName}
                            onChange={this.handleChange}
                        />
                    </label>
                    <br />
                    <label>
                        Date:
                        <input
                            type="date"
                            name="date"
                            value={date}
                            onChange={this.handleChange}
                        />
                    </label>
                    <br />
                    <label>
                        Claim Amount:
                        <input
                            type="number"
                            name="amount"
                            value={amount}
                            onChange={this.handleChange}
                        />
                    </label>
                    <br />
                    <label>
                        Purpose:
                        <input
                            type="text"
                            name="purpose"
                            value={purpose}
                            onChange={this.handleChange}
                        />
                    </label>
                    <br />
                    <label>
                        Invoice Image:
                        <input
                            type="file"
                            accept="image/*"
                            onChange={this.handleImageChange}
                        />
                    </label>
                    <br />
                    <label>
                        Follow Up Claim:
                        <input
                            type="checkbox"
                            name="followUp"
                            checked={followUp}
                            onChange={this.handleChange}
                        />
                    </label>
                    <br />
                    {followUp && (
                        <label>
                            Previous Claim ID:
                            <input
                                type="text"
                                name="previousClaimId"
                                value={previousClaimId}
                                onChange={this.handleChange}
                            />
                        </label>
                    )}
                    <br />
                    <button type="submit">
