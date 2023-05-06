import React, {useEffect, useState} from 'react';
import {Link} from 'react-router-dom';
import axios from 'axios';
 
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
    const [claims, setClaims] = useState([]);
    const [rerun, setRerun] = useState(false)
    useEffect(() => {
        const getClaims = async () => {

            const response = await axios.get('http://127.0.0.1:5000/claims/10011')
            const data = response.data.claims;
            console.log(data)
            setClaims(data);
        }
        getClaims()
    }, [rerun])

    const deleteClaim = async (claimid) => {
        await axios.delete(`http://127.0.0.1:5000/claims/${claimid}`)
        console.log(claimid)
        setRerun(prev => !prev)
    }
    

    return (
        <div>
        <br/>
            <h4>Employee Claiming Records</h4>
            <br/>
            <table width="80%" border="1px solid black">
                <thead id='tablehead'>
                    <tr>
                        <th>Status of Claim</th>
                        <th>Project ID</th>
                        <th>Claim ID</th>
                        <th>Currency</th>
                        <th>Delete Claim</th>
                    </tr>
                </thead>
                <tbody id='tablebody' style={{textAlign:"center"}}>
                    {claims.map(data => {
                        console.log(data)
                        if (data.status=='Approved') {
                            return <tr key={data['claim_id']}>
                                <td>{data.status}</td>
                                <td>{data['project_id']}</td>
                                <td>{data['claim_id']}</td>
                                <td>{data['currency_id']}</td>
                                <td onClick={() => {deleteClaim(data['claim_id'])}}>X</td>
                            </tr>
                        } else {
                            return <tr  key={data.ClaimID}>
                                <td>{data.status}</td>
                                <td>{data['project_id']}</td>
                                <td><Link to={`/updateClaim/${data['claim_id']}`}>{data['claim_id']}</Link></td>
                                <td>{data['currency_id']}</td>
                                <td onClick={() => {deleteClaim(data['claim_id'])}}>X</td>
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