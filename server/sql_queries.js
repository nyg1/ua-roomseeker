exports.getBuildingListSQL = `SELECT name FROM buildings;`;

exports.getTimesSQL = `
    SELECT b.bid, b.name, r.name,  FROM buildings AS b
    INNER JOIN rooms AS r ON r.bid = b.bid
    INNER JOIN times AS t ON t.bid = t.bid AND r.cid = t.cid
    GROUP BY b.bid;
`;