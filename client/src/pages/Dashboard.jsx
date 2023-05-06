import React from 'react';
import {Link} from 'react-router-dom';

function deleteClaim() {
    return 
}

const anotherData = [
        {"EmployeeID": "10011",
        "ExpenseDate": "2023-04-29T08:30:00+08:00",
        "Status": "Pending",
        "ClaimID": "11147",
        "ProjectID": "10001",
        "CurrencyID": "SGD",
        "Purpose": "Banking tech",  
        "AccountNumber": "3749137313"
    },
        {"EmployeeID": "10012",
        "ExpenseDate": "2023-04-20T08:30:00+08:00",
        "Status": "Approved",
        "ClaimID": "11145",
        "ProjectID": "10003",
        "CurrencyID": "SGD",
        "Purpose": "Operations",  
        "AccountNumber": "37491398273"
    },
        {"EmployeeID": "10010",
        "ExpenseDate": "2023-04-30T08:30:00+08:00",
        "Status": "Rejected",
        "ClaimID": "11143",
        "ProjectID": "10003",
        "CurrencyID": "SGD",
        "Purpose": "Banking tech",  
        "AccountNumber": "20191398273"
    }
]

const Dashboard = () => {
    return (
        <div>
        <br/>
            <h4>Employee Claiming Records</h4>
            <br/>
            <table width="80%" border="1px solid black">
                <thead>
                    <tr>
                        <th>Employee ID</th>
                        <th>Status of Claim</th>
                        <th>Project ID</th>
                        <th>Claim ID</th>
                        <th>Currency</th>
                        <th>Delete Claim</th>
                    </tr>
                </thead>
                <br/>
                <tbody style={{textAlign:"center"}}>
                    {anotherData.map(data => {
                        if (data.Status=='Approved') {
                            return <tr>
                                <td>{data.EmployeeID}</td>
                                <td>{data.Status}</td>
                                <td>{data.ProjectID}</td>
                                <td>{data.ClaimID}</td>
                                <td>{data.CurrencyID}</td>
                                <td onClick={deleteClaim}>X</td>
                            </tr>
                        } else {
                            return <tr>
                                <td>{data.EmployeeID}</td>
                                <td>{data.Status}</td>
                                <td>{data.ProjectID}</td>
                                <td><Link to={'/updateClaim/'}>{data.ClaimID}</Link></td>
                                <td>{data.CurrencyID}</td>
                                <td onClick={deleteClaim}>X</td>
                            </tr>
                        }
                    }
                    )}   
                </tbody>
            </table>
        </div>
    )
}

export default Dashboard;